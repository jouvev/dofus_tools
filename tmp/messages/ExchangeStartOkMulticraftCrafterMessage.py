class ExchangeStartOkMulticraftCrafterMessage:
   def __init__(self,input):
      self._skillIdFunc(input)
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhInt()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of ExchangeStartOkMulticraftCrafterMessage.skillId.")

   def resume(self):
      print("skillId :",self.skillId)
