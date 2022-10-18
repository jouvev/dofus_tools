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
    
    def readUnsignedByte(self):
        bits = self.read_next_bit(8)
        return int(bits,base=2)
    
    def readUnsignedInt(self):
        bits = self.read_next_bit(32)
        return int(bits,base=2)
    
    def readUTF(self):
        length = self.readUnsignedShort()
        bits = self.read_next_bit(length*8)
        res = "".join([chr(int(x,2)) for x in [bits[i:i+8] 
                                for i in range(0,len(bits), 8)
                                ]
                            ])
        return res
    
    def readUTFBytes(self,length):
        bits = self.read_next_bit(length*8)
        res = "".join([chr(int(x,2)) for x in [bits[i:i+8] 
                                for i in range(0,len(bits), 8)
                                ]
                            ])
        return res
    
    def readDouble(self):
        bits = self.read_next_bit(64)
        signe = -1 if bits[0]=="1" else 1
        exp = int(bits[1:12],base=2)-2**10+1
        mantisse = 1+int(bits[12:],base=2)/(2**52)
        return signe * 2**exp * mantisse
    
    def readFloat(self):
        bits = self.read_next_bit(32)
        signe = -1 if bits[0]=="1" else 1
        exp = int(bits[1:9],base=2)-2**7+1
        mantisse = 1+int(bits[9:],base=2)/(2**23)
        return signe * 2**exp * mantisse
    
    def readByte(self):
        bits = self.read_next_bit(8)
        value = int(bits,base=2)
        if (value > BYTE_MAX_VALUE):
            value -= UNSIGNED_BYTE_MAX_VALUE
        return value
    
    def readBytes(self,offset,length):
        res = []
        _ = self.read_next_bit(offset*8)#poubelle
        for _ in range(length):
            res.append(self.readByte())
        return res
    
    def readShort(self):
        bits = self.read_next_bit(16)
        value = int(bits,base=2)
        if (value > SHORT_MAX_VALUE):
            value -= UNSIGNED_SHORT_MAX_VALUE
        return value
    
    def readVarUhShort(self):
        return self.readVarShort()
    
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
    
    def readVarUhInt(self):
        return self.readVarInt()
    
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
    
    def readVarLong(self):
        b = 0
        result_low = 0
        result_high = 0
        i = 0
        while(True):
            b = self.readUnsignedByte()
            if(i == 28):
                break
            if(b < 128):
                result_low = result_low | (b << i)
                return result(result_low,result_high)
            result_low = result_low | ((b & 127) << i)
            i += 7
        if(b >= 128):
            b &= 127
            result_low =  result_low | (b << i)
            result_high = b >> 4
            i = 3
            while(True):
                b = self.readUnsignedByte()
                if(i < 32):
                    if(b < 128):
                        break
                    result_high =  result_high | ((b & 127) << i)
                i += 7
            result_high = result_high | (b << i)
            return result(result_low,result_high)
        result_low =  result_low | (b << i)
        result_high = b >> 4
        return result(result_low,result_high)
    
    def readVarUhLong(self):
        b = 0
        result_low = 0
        result_high = 0
        i = 0
        while(True):
            b = self.readUnsignedByte()
            if(i == 28):
                break
            if(b < 128):
                result_low = result_low | (b << i)
                return result(result_low,result_high)
            result_low = result_low | ((b & 127) << i)
            i += 7
        if(b >= 128):
            b &= 127
            result_low = result_low| (b << i)
            result_high = b >> 4
            i = 3
            while(True):
                b = self.readUnsignedByte()
                if(i < 32):
                    if(b < 128):
                        break
                    result_high = result_high | ((b & 127) << i)
                i += 7
            result_high = result_high | (b << i)
            return result(result_low,result_high)
        result_low = result_low | (b << i)
        result_high = b >> 4
        return result(result_low,result_high)
    
def result(low,high):
    return high * 4294967296 + low