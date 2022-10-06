import src.reseau.TypesFactory as pf
from src.reseau.types.Item import Item

class ObjectItemToSell(Item):
   def __init__(self,input):
      self.effects = []
      _id2 = 0
      _item2 = None
      super().__init__(input)
      self._objectGIDFunc(input)
      _effectsLen = input.readUnsignedShort()
      for _i2 in range(0,_effectsLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.effects.append(_item2)
      self._objectUIDFunc(input)
      self._quantityFunc(input)
      self._objectPriceFunc(input)
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemToSell.objectGID.")
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItemToSell.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemToSell.quantity.")
   
   def _objectPriceFunc(self,input) :
      self.objectPrice = input.readVarUhLong()
      if(self.objectPrice < 0 or self.objectPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element of ObjectItemToSell.objectPrice.")

   def resume(self):
      super().resume()
      print("objectGID :",self.objectGID)
      print("objectUID :",self.objectUID)
      print("quantity :",self.quantity)
      print("objectPrice :",self.objectPrice)
      for e in self.effects:
         e.resume()
