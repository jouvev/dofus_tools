import src.reseau.TypesFactory as pf

class ExchangeBidHouseInListAddedMessage:
   def __init__(self,input):
      self.effects = []
      self.prices = []
      _id4 = 0
      _item4 = None
      _val5 = None
      self._itemUIDFunc(input)
      self._objectGIDFunc(input)
      self._objectTypeFunc(input)
      _effectsLen = input.readUnsignedShort()
      for _i4 in range(0,_effectsLen):
         _id4 = input.readUnsignedShort()
         _item4 = pf.TypesFactory.get_instance_id(_id4,input)
         self.effects.append(_item4)
      _pricesLen = input.readUnsignedShort()
      for _i5 in range(0,_pricesLen):
         _val5 = input.readVarUhLong()
         if(_val5 < 0 or _val5 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val5 + ") on elements of prices.")
         self.prices.append(_val5)
   
   def _itemUIDFunc(self,input) :
      self.itemUID = input.readInt()
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ExchangeBidHouseInListAddedMessage.objectGID.")
   
   def _objectTypeFunc(self,input) :
      self.objectType = input.readInt()
      if(self.objectType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectType) + ") on element of ExchangeBidHouseInListAddedMessage.objectType.")

   def resume(self):
      print("itemUID :",self.itemUID)
      print("objectGID :",self.objectGID)
      print("objectType :",self.objectType)
      for e in self.effects:
         e.resume()
      print("prices :",self.prices)
