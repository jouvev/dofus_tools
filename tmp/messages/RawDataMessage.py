class RawDataMessage:
   def __init__(self,input):
      _contentLen = input.readVarInt()
      self.content = input.readBytes(0,_contentLen)