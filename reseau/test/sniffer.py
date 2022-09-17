import pyshark
import regex as re
from reseau.tools import *
from reseau.packet import Packet
from reseau.messagefactory import MessageFactory

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp src port 5555')
#bug si plusieurs dofus ouvert il faut focus un seul dst port
cap.sniff(packet_count=1)
dst_port = cap[0].tcp.dstport
print(dst_port)

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp src port 5555 and tcp dst port '+dst_port)

buffer = ""

#FILTER = "GameFightSynchronizeMessage"
FILTER = ""

list_name = ["Nighwin",
    "Jeandou" ,
    "Xox-elie" ,
    "Syllafarmn"]

re_exp = "("+"|".join(list_name)+")"

gamesynchro = None
turnlist = None

for packet in cap.sniff_continuously():
    try : 
        packet.tcp.payload
    except:
        continue 
    
    content = hexa_to_bin(packet)
    buffer += content
    stop = False
    rest = " "
    
    while(len(rest)>0):
        msg, rest, c = get_msg(buffer)
        if(c):
            p = Packet(msg)
            if("GameFightSynchronizeMessage".lower() in p.get_class().lower()):
                
                content = p.get_content()
                inst = MessageFactory.get_instance_id(p.packetid,content)
                gamesynchro = inst    
            elif("GameFightTurnListMessage".lower() in p.get_class().lower()):
                
                content = p.get_content()
                inst = MessageFactory.get_instance_id(p.packetid,content)
                turnlist = inst
                                

            buffer = buffer[len(msg):]
    if(gamesynchro and turnlist):
        id_name = dict()
        for f in gamesynchro.fighters:
            try:
                name = f.name
            except :
                continue
            id_name[f.contextualid] = f.name
            
        orderlist = [id_name[conid] for conid in turnlist.ids if conid in id_name]
        print(orderlist)
        gamesynchro = None
        turnlist = None
    if(stop):
        break

