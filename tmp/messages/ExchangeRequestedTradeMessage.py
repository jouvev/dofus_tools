from tmp.messages.ExchangeRequestedMessage import ExchangeRequestedMessage
class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
   def __init__(self,input):
      super().__init__(input)
      self._sourceFunc(input)
      self._targetFunc(input)
   
   def _sourceFunc(self,input) :
      self.source = input.readVarUhLong()
      if(self.source < 0 or self.source > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.source + ") on element of ExchangeRequestedTradeMessage.source.")
   
   def _targetFunc(self,input) :
      self.target = input.readVarUhLong()
      if(self.target < 0 or self.target > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.target + ") on element of ExchangeRequestedTradeMessage.target.")