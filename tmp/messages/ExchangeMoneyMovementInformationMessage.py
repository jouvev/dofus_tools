class ExchangeMoneyMovementInformationMessage:
   def __init__(self,input):
      self._limitFunc(input)
   
   def _limitFunc(self,input) :
      self.limit = input.readVarUhLong()
      if(self.limit < 0 or self.limit > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.limit + ") on element of ExchangeMoneyMovementInformationMessage.limit.")