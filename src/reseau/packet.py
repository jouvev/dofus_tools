from src.reseau.custominput import CustomInput

class Packet:
    def __init__(self, input):
        self.all = input
        self.packetid, self.lentype, self.len = self._read_header(self.all)

    def _read_header(self,input):
        packetid = int(input[:14],base=2)
        lentype = int(input[14:16],base=2)
        l = 0
        if(lentype > 0):
            l = int(input[16:16+lentype*8],base=2)
        return packetid, lentype, l
    
    def get_packet_id(self):
        return self.packetid
    
    def get_content(self):
        header_len = 16+self.lentype*8
        return CustomInput(self.all[header_len:])
    
class RequestPacket:
    def __init__(self, input):
        self.all = input
        self.packetid, self.lentype, self.len,self.id = self._read_header(self.all)

    def _read_header(self,input):
        packetid = int(input[:14],base=2)
        lentype = int(input[14:16],base=2)
        l = 0
        tmp = int(input[16:16+32],base=2)
        if(lentype > 0):
            l = int(input[16+32:16+32+lentype*8],base=2)
        return packetid, lentype, l, tmp
    
    def get_packet_id(self):
        return self.packetid
    
    def get_content(self):
        header_len = 16+32+self.lentype*8
        return CustomInput(self.all[header_len:])
