from scapy.all import *
from src.reseau.tools import *
from src.reseau.packet import Packet
from src.reseau.MessagesFactory import MessagesFactory
import time

class Sniffer(AsyncSniffer):
    def __init__(self):
        AsyncSniffer.__init__(self, iface="Ethernet", filter=f"tcp src port 5555", prn=self.packet_callback)
        self.buffer = ""
        
    def packet_callback(self,packet):
        if not packet.haslayer(Raw):
            return
        v = bytes(packet["TCP"].payload).hex(":")
        data = hexa_to_bin(v)
        self.buffer += data
        rest = ' '
        while(len(rest) > 0) :
            msg, rest, c = get_msg(self.buffer)
            if(c):
                if(int(msg) == 0):
                    self.buffer = self.buffer[len(msg):]
                    continue
                p = Packet(msg)
                pname = MessagesFactory.id_class[str(p.packetid)].__name__
                self.buffer = self.buffer[len(msg):]
                if("MapComplementaryInformationsDataMessage".lower() in pname.lower()):
                    print("################ ->",pname)
                    msg = MessagesFactory.get_instance_id(p.packetid,p.get_content())
                    print('-------- ACTORS --------')
                    for a in msg.actors:
                        try :
                            print(a.npcId)
                        except:
                            continue
            
t = Sniffer()
t.start()
t.join()

    