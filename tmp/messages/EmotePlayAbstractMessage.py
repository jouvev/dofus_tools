class EmotePlayAbstractMessage:
   def __init__(self,input):
      self._emoteIdFunc(input)
      self._emoteStartTimeFunc(input)
   
   def _emoteIdFunc(self,input) :
      self.emoteId = input.readUnsignedShort()
      if(self.emoteId < 0 or self.emoteId > 65535) :
         raise RuntimeError("Forbidden value (" + self.emoteId + ") on element of EmotePlayAbstractMessage.emoteId.")
   
   def _emoteStartTimeFunc(self,input) :
      self.emoteStartTime = input.readDouble()
      if(self.emoteStartTime < -9007199254740992 or self.emoteStartTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.emoteStartTime + ") on element of EmotePlayAbstractMessage.emoteStartTime.")