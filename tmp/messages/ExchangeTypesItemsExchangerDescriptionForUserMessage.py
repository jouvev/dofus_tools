from tmp.types.BidExchangerObjectInfo import BidExchangerObjectInfo
class ExchangeTypesItemsExchangerDescriptionForUserMessage:
   def __init__(self,input):
      self.itemTypeDescriptions = []
      _item3 = None
      self._objectGIDFunc(input)
      self._objectTypeFunc(input)
      _itemTypeDescriptionsLen = input.readUnsignedShort()
      for _i3 in range(0,_itemTypeDescriptionsLen):
         _item3 = BidExchangerObjectInfo(input)
         self.itemTypeDescriptions.append(_item3)
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectGID + ") on element of ExchangeTypesItemsExchangerDescriptionForUserMessage.objectGID.")
   
   def _objectTypeFunc(self,input) :
      self.objectType = input.readInt()
      if(self.objectType < 0) :
         raise RuntimeError("Forbidden value (" + self.objectType + ") on element of ExchangeTypesItemsExchangerDescriptionForUserMessage.objectType.")