import pyshark
from src.reseau.tools import *
from src.reseau.packet import RequestPacket
from src.reseau.MessagesFactory import MessagesFactory
import time
import mouse

s = 0 

def get_time():
    global s 
    s = time.time()
    
mouse.on_click(lambda : get_time())

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp dst port 5555')

buffer = dict()

gamesynchro = dict()
turnlist = dict()

for packet in cap.sniff_continuously():
    f=time.time()
    try : 
        p = packet.tcp.payload
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
            pname = MessagesFactory.id_class[str(p.packetid)].__name__
            buffer[dst_port] = buffer[dst_port][len(msg):]
            if("".lower() in pname.lower()):
                print("###### =>",pname)
                msg = MessagesFactory.get_instance_id(p.packetid,p.get_content())
                msg.resume()

            