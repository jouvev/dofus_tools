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

cap = pyshark.LiveCapture(interface='Ethernet')

buffer = dict()

gamesynchro = dict()
turnlist = dict()

def parse_packet(packet):
    f=time.time()
    try :
        if(packet.tcp.dstport != "5555"):
            return
        p = packet.tcp.payload
    except:
        return
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
            print("###### =>",pname,p.len)
            if("GameMapMovementRequestMessage".lower() in pname.lower()):
                t = packet.sniff_timestamp
                f2 = time.time()
                print("time : ",float(t)-s)
                print("time : ",f-s)
                print("time : ",f2-s)
                print("time : ",f2-f)

cap.apply_on_packets(lambda p : parse_packet(p))
            