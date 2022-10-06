from threading import Thread
import pyshark
from src.reseau.tools import *
from src.reseau.packet import Packet
from src.reseau.MessagesFactory import MessagesFactory
import asyncio



class PacketSniffer(Thread):
    def __init__(self,manager):
        Thread.__init__(self)
        self.handler = manager.dofus_handler
        self.manager = manager
        self.running = True
        
    def stop(self):
        self.running = False
    
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp src port 5555')
        buffer = dict()

        gamesynchro = dict()
        turnlist = dict()

        for packet in cap.sniff_continuously():
            if(not self.running): 
                break
            try : 
                packet.tcp.payload
            except:
                continue 
            dst_port = packet.tcp.dstport
            
            content = hexa_to_bin(packet)
            
            if( dst_port in buffer):
                buffer[dst_port] += content
            else:
                buffer[dst_port] = content

            rest = " "
            
            while(len(rest)>0):
                msg, rest, c = get_msg(buffer[dst_port])
                if(c):
                    p = Packet(msg)
                    #print(MessageFactory.id_class[str(p.packetid)],dst_port)
                    if("GameFightSynchronizeMessage".lower() in MessagesFactory.id_class[str(p.packetid)].__class__.__name__.lower()):
                        
                        content = p.get_content()
                        inst = MessagesFactory.get_instance_id(p.packetid,content)
                        gamesynchro[dst_port] = inst    
                    elif("GameFightTurnListMessage".lower() in MessagesFactory.id_class[str(p.packetid)].__class__.__name__.lower()):
                        
                        content = p.get_content()
                        inst = MessagesFactory.get_instance_id(p.packetid,content)
                        turnlist[dst_port] = inst
                                        

                    buffer[dst_port] = buffer[dst_port][len(msg):]
                    
            supp = []
            for dst_port in gamesynchro.keys():
                if(dst_port in turnlist.keys()):
                    id_hwnd = dict()
                    for f in gamesynchro[dst_port].fighters:
                        try:
                            hwnd = self.handler.get_hwnd_by_name(f.name)
                        except :
                            continue
                        id_hwnd[f.contextualid] = hwnd
                        
                    orderlist = [id_hwnd[conid] for conid in turnlist[dst_port].ids if conid in id_hwnd]
                    self.handler.update_order(orderlist)
                    supp.append(dst_port)
            
            for dst_port in supp:
                del gamesynchro[dst_port]
                del turnlist[dst_port]
        
        cap.close()
        