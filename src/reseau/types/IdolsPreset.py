from src.reseau.types.Preset import Preset

class IdolsPreset(Preset):
   def __init__(self,input):
      self.idolIds = []
      _val2 = 0
      super().__init__(input)
      self._iconIdFunc(input)
      _idolIdsLen = input.readUnsignedShort()
      for _i2 in range(0,_idolIdsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of idolIds.")
         self.idolIds.append(_val2)
   
   def _iconIdFunc(self,input) :
      self.iconId = input.readShort()
      if(self.iconId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.iconId) + ") on element of IdolsPreset.iconId.")

   def resume(self):
      super().resume()
      print("iconId :",self.iconId)
      print("idolIds :",self.idolIds)
