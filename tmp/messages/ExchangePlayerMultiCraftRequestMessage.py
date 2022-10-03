from tmp.messages.ExchangeRequestMessage import ExchangeRequestMessage
class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetFunc(input)
      self._skillIdFunc(input)
   
   def _targetFunc(self,input) :
      self.target = input.readVarUhLong()
      if(self.target < 0 or self.target > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.target + ") on element of ExchangePlayerMultiCraftRequestMessage.target.")
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhInt()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + self.skillId + ") on element of ExchangePlayerMultiCraftRequestMessage.skillId.")