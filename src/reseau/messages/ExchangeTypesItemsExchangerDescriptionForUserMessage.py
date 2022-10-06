from src.reseau.types.BidExchangerObjectInfo import BidExchangerObjectInfo

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
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ExchangeTypesItemsExchangerDescriptionForUserMessage.objectGID.")
   
   def _objectTypeFunc(self,input) :
      self.objectType = input.readInt()
      if(self.objectType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectType) + ") on element of ExchangeTypesItemsExchangerDescriptionForUserMessage.objectType.")

   def resume(self):
      print("objectGID :",self.objectGID)
      print("objectType :",self.objectType)
      for e in self.itemTypeDescriptions:
         e.resume()
