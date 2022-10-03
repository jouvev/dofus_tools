from tmp.messages.ExchangeObjectMessage import ExchangeObjectMessage
class ExchangeObjectRemovedMessage(ExchangeObjectMessage):
   def __init__(self,input):
      super().__init__(input)
      self._objectUIDFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectUID + ") on element of ExchangeObjectRemovedMessage.objectUID.")