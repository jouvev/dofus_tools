class ExchangeStartOkMulticraftCustomerMessage:
   def __init__(self,input):
      self._skillIdFunc(input)
      self._crafterJobLevelFunc(input)
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhInt()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of ExchangeStartOkMulticraftCustomerMessage.skillId.")
   
   def _crafterJobLevelFunc(self,input) :
      self.crafterJobLevel = input.readUnsignedByte()
      if(self.crafterJobLevel < 0 or self.crafterJobLevel > 255) :
         raise RuntimeError("Forbidden value (" + str(self.crafterJobLevel) + ") on element of ExchangeStartOkMulticraftCustomerMessage.crafterJobLevel.")

   def resume(self):
      print("skillId :",self.skillId)
      print("crafterJobLevel :",self.crafterJobLevel)
