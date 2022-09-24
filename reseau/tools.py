def hexa_to_bin(packet):
    content = str(packet.tcp.payload).replace(':','')
    content = bin(int(str(packet.tcp.payload).replace(':',''),base=16))[2:].zfill(4*len(str(packet.tcp.payload).replace(':','')))
    return content

def read_next_bit(content,n):
    bit = content[:n]
    return bit, content[n:]

def get_msg(input):
    l = 0
    lentype = 0
    
    if len(input) >= 16:
        lentype = int(input[14:16],base=2)*8
    
    if(lentype > 0 and len(input) >= 16+lentype):
        l = int(input[16:16+lentype],base=2)*8
    
    if(len(input)>=l+lentype+16):
        complet = True
        msg = input[:16+lentype+l]
        rest = input[16+lentype+l:]
    else :
        complet = False
        msg = input
        rest = ""
    
    return msg , rest, complet

def get_req(input):
    l = 0
    lentype = 0
    
    if len(input) >= 16:
        lentype = int(input[14:16],base=2)*8
    
    if(lentype > 0 and len(input) >= 16+lentype):
        l = int(input[16+32:16+32+lentype],base=2)*8
    
    if(len(input)>=l+32+lentype+16):
        complet = True
        msg = input[:16+32+lentype+l]
        rest = input[16+32+lentype+l:]
    else :
        complet = False
        msg = input
        rest = ""
    
    return msg , rest, complet