from tmp.messages.ExchangeObjectMessage import ExchangeObjectMessage

class ExchangeObjectRemovedFromBagMessage(ExchangeObjectMessage):
   def __init__(self,input):
      super().__init__(input)
      self._objectUIDFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ExchangeObjectRemovedFromBagMessage.objectUID.")

   def resume(self):
      super().resume()
      print("objectUID :",self.objectUID)
