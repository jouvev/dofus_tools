class EmotePlayRequestMessage:
   def __init__(self,input):
      self._emoteIdFunc(input)
   
   def _emoteIdFunc(self,input) :
      self.emoteId = input.readUnsignedShort()
      if(self.emoteId < 0 or self.emoteId > 65535) :
         raise RuntimeError("Forbidden value (" + str(self.emoteId) + ") on element of EmotePlayRequestMessage.emoteId.")

   def resume(self):
      print("emoteId :",self.emoteId)
