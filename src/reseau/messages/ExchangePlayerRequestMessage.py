from src.reseau.messages.ExchangeRequestMessage import ExchangeRequestMessage

class ExchangePlayerRequestMessage(ExchangeRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetFunc(input)
   
   def _targetFunc(self,input) :
      self.target = input.readVarUhLong()
      if(self.target < 0 or self.target > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.target) + ") on element of ExchangePlayerRequestMessage.target.")

   def resume(self):
      super().resume()
      print("target :",self.target)
