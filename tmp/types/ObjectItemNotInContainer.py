import tmp.TypesFactory as pf
from tmp.types.Item import Item
class ObjectItemNotInContainer(Item):
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
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectGID + ") on element of ObjectItemNotInContainer.objectGID.")
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectUID + ") on element of ObjectItemNotInContainer.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ObjectItemNotInContainer.quantity.")