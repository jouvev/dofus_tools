class ExchangeBidHouseInListRemovedMessage:
   def __init__(self,input):
      self._itemUIDFunc(input)
      self._objectGIDFunc(input)
      self._objectTypeFunc(input)
   
   def _itemUIDFunc(self,input) :
      self.itemUID = input.readInt()
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectGID + ") on element of ExchangeBidHouseInListRemovedMessage.objectGID.")
   
   def _objectTypeFunc(self,input) :
      self.objectType = input.readInt()
      if(self.objectType < 0) :
         raise RuntimeError("Forbidden value (" + self.objectType + ") on element of ExchangeBidHouseInListRemovedMessage.objectType.")