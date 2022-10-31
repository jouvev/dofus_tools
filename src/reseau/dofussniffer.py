from threading import Thread,Lock
import pyshark
from src.reseau.tools import *
from src.reseau.packet import Packet
import asyncio
import logging

class PacketSniffer(Thread):
    def __init__(self,dofus):
        Thread.__init__(self)
        self.running = True
        self.port = dofus.port
        self.dofus = dofus
        self.buffer = ""
        self.lock = Lock()
        
    def stop(self):
        self.running = False
        
    def change_port(self, port):
        with self.lock:
            self.port = port
            self.buffer = ""
    
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter=f'tcp src port 5555')

        for packet in cap.sniff_continuously():
            with self.lock:
                if(not self.running):
                    break
                
                if(not (self.port != "" and int(packet.tcp.dstport) == int(self.port))):
                    continue
                
                try : 
                    p = packet.tcp.payload
                except:
                    continue 

                payload = hexa_to_bin(p)
                self.buffer += payload
                rest = " "
                
                while(len(rest)>0):
                    msg, rest, c = get_msg(self.buffer)
                    if(c):
                        p = Packet(msg)
                        try :
                            self.dofus.packet_received(p)
                        except KeyError as e:
                            logging.error("Error with packet" + str(e))
                            self.buffer = ""
                            break
                        self.buffer = self.buffer[len(msg):]