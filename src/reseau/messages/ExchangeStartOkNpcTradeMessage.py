class ExchangeStartOkNpcTradeMessage:
   def __init__(self,input):
      self._npcIdFunc(input)
   
   def _npcIdFunc(self,input) :
      self.npcId = input.readDouble()
      if(self.npcId < -9007199254740992 or self.npcId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element of ExchangeStartOkNpcTradeMessage.npcId.")

   def resume(self):
      print("npcId :",self.npcId)
