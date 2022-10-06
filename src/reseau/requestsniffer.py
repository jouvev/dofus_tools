from threading import Thread
import pyshark
from src.reseau.tools import *
from src.reseau.packet import RequestPacket
import asyncio
from src.reseau.MessagesFactory import MessagesFactory


class RequestSniffer(Thread):
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
        
        cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp dst port 5555')
        buffer = dict()

        for packet in cap.sniff_continuously():
            if(not self.running): 
                break
            try : 
                packet.tcp.payload
            except:
                continue 
            dst_port = packet.tcp.srcport
            
            content = hexa_to_bin(packet)
            
            if( dst_port in buffer):
                buffer[dst_port] += content
            else:
                buffer[dst_port] = content

            rest = " "
            
            while(len(rest)>0):
                msg, rest, c = get_req(buffer[dst_port])
                if(c):
                    p = RequestPacket(msg)
                    #print(p.packetid,id_class[str(p.packetid)],p.lentype,p.len,dst_port,p.id)
                    buffer[dst_port] = buffer[dst_port][len(msg):]
                    if("GameMapMovementConfirmMessage" in MessagesFactory.id_class[str(p.packetid)].__name__.lower() ):
                        d = self.handler.get_dofus_by_port(dst_port)
                        d.confirm = True
                    elif("NpcDialog" in MessagesFactory.id_class[str(p.packetid)].__name__.lower() ):
                        self.handler.get_dofus_by_port(dst_port).confirm = True
        
        cap.close()
        