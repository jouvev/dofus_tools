import pyshark
import regex as re
from src.reseau.tools import *
from src.reseau.packet import Packet, RequestPacket
from src.reseau.messagefactory import MessageFactory
import json

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp dst port 5555')
"""#bug si plusieurs dofus ouvert il faut focus un seul dst port
cap.sniff(packet_count=1)
dst_port = cap[0].tcp.dstport
print(dst_port)

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp src port 5555 and tcp dst port '+dst_port)"""

buffer = dict()

gamesynchro = dict()
turnlist = dict()

id_class = json.load(open("reseau/requestid.json"))

for packet in cap.sniff_continuously():
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
            print(p.packetid,id_class[str(p.packetid)],p.lentype,p.len,dst_port,p.id)
            buffer[dst_port] = buffer[dst_port][len(msg):]
            """if("GameFightSynchronizeMessage".lower() in MessageFactory.id_class[str(p.packetid)].lower()):
                
                content = p.get_content()
                inst = MessageFactory.get_instance_id(p.packetid,content)
                gamesynchro[dst_port] = inst    
            elif("GameFightTurnListMessage".lower() in MessageFactory.id_class[str(p.packetid)].lower()):
                
                content = p.get_content()
                inst = MessageFactory.get_instance_id(p.packetid,content)
                turnlist[dst_port] = inst
                                

            
    supp = []
    for dst_port in gamesynchro.keys():
        if(dst_port in turnlist.keys()):
            id_name = dict()
            for f in gamesynchro[dst_port].fighters:
                try:
                    name = f.name
                except :
                    continue
                id_name[f.contextualid] = f.name
                
            orderlist = [id_name[conid] for conid in turnlist[dst_port].ids if conid in id_name]
            print(orderlist)
            supp.append(dst_port)
    
    for dst_port in supp:
        del gamesynchro[dst_port]
        del turnlist[dst_port]"""

