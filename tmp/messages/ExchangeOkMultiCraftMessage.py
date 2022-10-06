class ExchangeOkMultiCraftMessage:
   def __init__(self,input):
      self._initiatorIdFunc(input)
      self._otherIdFunc(input)
      self._roleFunc(input)
   
   def _initiatorIdFunc(self,input) :
      self.initiatorId = input.readVarUhLong()
      if(self.initiatorId < 0 or self.initiatorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.initiatorId) + ") on element of ExchangeOkMultiCraftMessage.initiatorId.")
   
   def _otherIdFunc(self,input) :
      self.otherId = input.readVarUhLong()
      if(self.otherId < 0 or self.otherId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.otherId) + ") on element of ExchangeOkMultiCraftMessage.otherId.")
   
   def _roleFunc(self,input) :
      self.role = input.readByte()

   def resume(self):
      print("initiatorId :",self.initiatorId)
      print("otherId :",self.otherId)
      print("role :",self.role)
