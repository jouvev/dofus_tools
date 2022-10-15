import pyshark
from src.reseau.tools import *
from src.reseau.packet import Packet
from src.reseau.MessagesFactory import MessagesFactory
import json

mappostmp = json.load(open("ressources/MapPositions.json","r"))
mappos = dict()
for m in mappostmp:
    mapid = m["id"]
    x,y = m["posX"],m["posY"]
    mappos[mapid] = (x,y)
    
idtotext = json.load(open("ressources/i18n_fr.json","r",encoding="latin-1"))

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter='tcp src port 5555')

buffer = dict()

gamesynchro = dict()
turnlist = dict()

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
            pname = MessagesFactory.id_class[str(p.packetid)].__name__
            buffer[dst_port] = buffer[dst_port][len(msg):]
            if("currentmap".lower() in pname.lower()):
                print(pname)
                msg = MessagesFactory.get_instance_id(p.packetid,p.get_content())
                msg.resume()
                print("pos",mappos[msg.mapId])

            