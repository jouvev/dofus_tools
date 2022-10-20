from threading import Thread
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
        
    def stop(self):
        self.running = False
    
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter=f'tcp src port 5555 and dst port {self.port}')
        buffer = ""

        for packet in cap.sniff_continuously():
            if(not self.running):
                break
            
            try : 
                packet.tcp.payload
            except:
                continue 

            payload = hexa_to_bin(packet)
            buffer += payload
            rest = " "
            
            while(len(rest)>0):
                msg, rest, c = get_msg(buffer)
                if(c):
                    p = Packet(msg)
                    self.dofus.packet_received(p)
                    buffer = buffer[len(msg):]
        
        cap.close()
        