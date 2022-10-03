class ExchangeStartOkMulticraftCrafterMessage:
   def __init__(self,input):
      self._skillIdFunc(input)
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhInt()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + self.skillId + ") on element of ExchangeStartOkMulticraftCrafterMessage.skillId.")