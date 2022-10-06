class NetworkDataContainerMessage:
   def __init__(self,input):
      _contentLen = input.readVarInt()
      tmpBuffer = input.readBytes(0,_contentLen)
      self.content = tmpBuffer

   def resume(self):
      pass