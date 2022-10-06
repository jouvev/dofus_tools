from tmp.messages.ExchangeObjectMessage import ExchangeObjectMessage

class ExchangeObjectsRemovedMessage(ExchangeObjectMessage):
   def __init__(self,input):
      self.objectUID = []
      _val1 = 0
      super().__init__(input)
      _objectUIDLen = input.readUnsignedShort()
      for _i1 in range(0,_objectUIDLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of objectUID.")
         self.objectUID.append(_val1)

   def resume(self):
      super().resume()
      print("objectUID :",self.objectUID)
