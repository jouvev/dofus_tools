from tmp.types.Preset import Preset
class EntitiesPreset(Preset):
   def __init__(self,input):
      self.entityIds = []
      _val2 = 0
      super().__init__(input)
      self._iconIdFunc(input)
      _entityIdsLen = input.readUnsignedShort()
      for _i2 in range(0,_entityIdsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of entityIds.")
         self.entityIds.append(_val2)
   
   def _iconIdFunc(self,input) :
      self.iconId = input.readShort()
      if(self.iconId < 0) :
         raise RuntimeError("Forbidden value (" + self.iconId + ") on element of EntitiesPreset.iconId.")