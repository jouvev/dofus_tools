from tmp.messages.ExchangeReadyMessage import ExchangeReadyMessage

class FocusedExchangeReadyMessage(ExchangeReadyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._focusActionIdFunc(input)
   
   def _focusActionIdFunc(self,input) :
      self.focusActionId = input.readVarUhInt()
      if(self.focusActionId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.focusActionId) + ") on element of FocusedExchangeReadyMessage.focusActionId.")

   def resume(self):
      super().resume()
      print("focusActionId :",self.focusActionId)
