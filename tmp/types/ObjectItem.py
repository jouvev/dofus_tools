import tmp.TypesFactory as pf
from tmp.types.Item import Item

class ObjectItem(Item):
   def __init__(self,input):
      self.effects = []
      _id3 = 0
      _item3 = None
      super().__init__(input)
      self._positionFunc(input)
      self._objectGIDFunc(input)
      _effectsLen = input.readUnsignedShort()
      for _i3 in range(0,_effectsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.effects.append(_item3)
      self._objectUIDFunc(input)
      self._quantityFunc(input)
   
   def _positionFunc(self,input) :
      self.position = input.readShort()
      if(self.position < 0) :
         raise RuntimeError("Forbidden value (" + str(self.position) + ") on element of ObjectItem.position.")
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItem.objectGID.")
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItem.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItem.quantity.")

   def resume(self):
      super().resume()
      print("position :",self.position)
      print("objectGID :",self.objectGID)
      print("objectUID :",self.objectUID)
      print("quantity :",self.quantity)
      for e in self.effects:
         e.resume()
