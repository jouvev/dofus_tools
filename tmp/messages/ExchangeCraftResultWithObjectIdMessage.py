from tmp.messages.ExchangeCraftResultMessage import ExchangeCraftResultMessage

class ExchangeCraftResultWithObjectIdMessage(ExchangeCraftResultMessage):
   def __init__(self,input):
      super().__init__(input)
      self._objectGenericIdFunc(input)
   
   def _objectGenericIdFunc(self,input) :
      self.objectGenericId = input.readVarUhInt()
      if(self.objectGenericId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGenericId) + ") on element of ExchangeCraftResultWithObjectIdMessage.objectGenericId.")

   def resume(self):
      super().resume()
      print("objectGenericId :",self.objectGenericId)
