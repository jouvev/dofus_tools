import tmp.TypesFactory as pf
from tmp.types.Item import Item

class ObjectItemMinimalInformation(Item):
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
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemMinimalInformation.objectGID.")

   def resume(self):
      super().resume()
      print("objectGID :",self.objectGID)
      for e in self.effects:
         e.resume()
