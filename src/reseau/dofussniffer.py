from scapy.all import AsyncSniffer, Raw
from src.reseau.tools import *
from src.reseau.packet import Packet

class PacketSniffer(AsyncSniffer):
    def __init__(self, dofus):
        AsyncSniffer.__init__(self, iface="Ethernet", filter=f"tcp src port 5555 and tcp dst port {dofus.port}", prn=self.packet_callback)
        self.buffer = ""
        self.dofus = dofus
        
    def packet_callback(self,packet):
        v = bytes(packet["TCP"].payload).hex(":")
        if v == "00:00:00:00:00:00" or v == '':
            return
        data = hexa_to_bin(v)
        self.buffer += data
        rest = ' '
        while(len(rest) > 0) :
            msg, rest, c = get_msg(self.buffer)
            if(int(msg) == 0):
                    self.buffer = self.buffer[len(msg):]
                    continue
            if(c):
                p = Packet(msg)
                self.dofus.packet_received(p)
                self.buffer = self.buffer[len(msg):]