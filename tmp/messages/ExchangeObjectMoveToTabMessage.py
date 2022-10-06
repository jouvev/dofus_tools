class ExchangeObjectMoveToTabMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._quantityFunc(input)
      self._tabNumberFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ExchangeObjectMoveToTabMessage.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarInt()
   
   def _tabNumberFunc(self,input) :
      self.tabNumber = input.readVarUhInt()
      if(self.tabNumber < 0) :
         raise RuntimeError("Forbidden value (" + str(self.tabNumber) + ") on element of ExchangeObjectMoveToTabMessage.tabNumber.")

   def resume(self):
      print("objectUID :",self.objectUID)
      print("quantity :",self.quantity)
      print("tabNumber :",self.tabNumber)
