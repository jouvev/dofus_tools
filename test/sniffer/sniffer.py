import pyshark
from src.reseau.tools import *
from src.reseau.packet import Packet
from tmp.MessagesFactory import MessagesFactory
import json

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp src port 5555')

buffer = dict()

gamesynchro = dict()
turnlist = dict()

id_class = json.load(open("tmp/msg.json"))

for packet in cap.sniff_continuously():
    try : 
        p = packet.tcp.payload
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
            print(p.packetid,id_class[str(p.packetid)],p.lentype,p.len,dst_port)
            buffer[dst_port] = buffer[dst_port][len(msg):]
            MessagesFactory.get_instance_id(p.packetid,p.get_content())

            