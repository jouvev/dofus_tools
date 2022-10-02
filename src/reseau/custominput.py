INT_SIZE = 32
MASK_10000000 = 128
MASK_01111111 = 127
CHUNCK_BIT_SIZE = 7
UNSIGNED_SHORT_MAX_VALUE = 65536
SHORT_MAX_VALUE = 32767
SHORT_SIZE = 16
UNSIGNED_INT_MAX_VALUE = 4294967296
INT_MAX_VALUE = 2147483647
BYTE_MAX_VALUE = 127
UNSIGNED_BYTE_MAX_VALUE = 256


class CustomInput:
    def __init__(self, content):
        self.content = content
        self.pointeur = 0
        
    def __len__(self):
        return len(self.content)
        
    def get_brut_content(self):
        return self.content
        
    def read_next_bit(self, n):
        if(n<0):
            raise RuntimeError("n must be positive in read_next_bit")
        bit = self.content[self.pointeur:self.pointeur+n]
        self.pointeur += n
        return bit
    
    def readUnsignedShort(self):
        bits = self.read_next_bit(16)
        return int(bits,base=2)
    
    def readUTF(self):
        length = self.readUnsignedShort()
        bits = self.read_next_bit(length*8)
        res = "".join([chr(int(x,2)) for x in [bits[i:i+8] 
                                for i in range(0,len(bits), 8)
                                ]
                            ])
        return res
    
    def readDouble(self):
        bits = self.read_next_bit(64)
        signe = -1 if bits[0] else 1
        exp = int(bits[1:12],base=2)-2**10+1
        mantisse = 1+int(bits[12:],base=2)/(2**52)
        return signe * 2**exp * mantisse
    
    def readByte(self):
        bits = self.read_next_bit(8)
        value = int(bits,base=2)
        if (value > BYTE_MAX_VALUE):
            value -= UNSIGNED_BYTE_MAX_VALUE
        return value
    
    def readShort(self):
        bits = self.read_next_bit(16)
        value = int(bits,base=2)
        if (value > SHORT_MAX_VALUE):
            value -= UNSIGNED_SHORT_MAX_VALUE
        return value
    
    def readVarShort(self):
        b = 0
        value = 0
        offset = 0
        hasNext = False
        while(offset < SHORT_SIZE):
            b = self.readByte()
            hasNext = (b & MASK_10000000) == MASK_10000000
            if(offset > 0):
                value += (b & MASK_01111111) << offset
            else:
                value += b & MASK_01111111
            offset += CHUNCK_BIT_SIZE
            if( not hasNext):
                if (value > SHORT_MAX_VALUE):
                    value -= UNSIGNED_SHORT_MAX_VALUE
                return value
        raise RuntimeError("Too much data")
    
    def readInt(self):
        bits = self.read_next_bit(32)
        value = int(bits,base=2)
        if value > INT_MAX_VALUE:
            value -= UNSIGNED_INT_MAX_VALUE
        return value
    
    def readBoolean(self):
        bits = self.read_next_bit(8)
        return bool(int(bits,base=2))
    
    def readVarInt(self):
        b = 0
        value = 0
        offset = 0
        hasNext = False
        while(offset < INT_SIZE):
            b = self.readByte()
            hasNext = (b & MASK_10000000) == MASK_10000000
            if(offset > 0):
                value += (b & MASK_01111111) << offset
            else:
                value += b & MASK_01111111
            offset += CHUNCK_BIT_SIZE
            if( not hasNext):
                return value
        raise RuntimeError("Too much data")