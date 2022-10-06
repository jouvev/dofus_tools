from tmp.types.HumanOption import HumanOption

class HumanOptionEmote(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self._emoteIdFunc(input)
      self._emoteStartTimeFunc(input)
   
   def _emoteIdFunc(self,input) :
      self.emoteId = input.readUnsignedShort()
      if(self.emoteId < 0 or self.emoteId > 65535) :
         raise RuntimeError("Forbidden value (" + str(self.emoteId) + ") on element of HumanOptionEmote.emoteId.")
   
   def _emoteStartTimeFunc(self,input) :
      self.emoteStartTime = input.readDouble()
      if(self.emoteStartTime < -9007199254740992 or self.emoteStartTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.emoteStartTime) + ") on element of HumanOptionEmote.emoteStartTime.")

   def resume(self):
      super().resume()
      print("emoteId :",self.emoteId)
      print("emoteStartTime :",self.emoteStartTime)
