class GuildPaddockRemovedMessage:
   def __init__(self,input):
      self._paddockIdFunc(input)
   
   def _paddockIdFunc(self,input) :
      self.paddockId = input.readDouble()
      if(self.paddockId < 0 or self.paddockId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.paddockId) + ") on element of GuildPaddockRemovedMessage.paddockId.")

   def resume(self):
      print("paddockId :",self.paddockId)
