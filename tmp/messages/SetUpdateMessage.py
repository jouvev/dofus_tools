import tmp.TypesFactory as pf
class SetUpdateMessage:
   def __init__(self,input):
      self.setObjects = []
      self.setEffects = []
      _val2 = 0
      _id3 = 0
      _item3 = None
      self._setIdFunc(input)
      _setObjectsLen = input.readUnsignedShort()
      for _i2 in range(0,_setObjectsLen):
         _val2 = input.readVarUhInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of setObjects.")
         self.setObjects.append(_val2)
      _setEffectsLen = input.readUnsignedShort()
      for _i3 in range(0,_setEffectsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.setEffects.append(_item3)
   
   def _setIdFunc(self,input) :
      self.setId = input.readVarUhShort()
      if(self.setId < 0) :
         raise RuntimeError("Forbidden value (" + self.setId + ") on element of SetUpdateMessage.setId.")