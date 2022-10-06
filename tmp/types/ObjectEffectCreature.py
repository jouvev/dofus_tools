from tmp.types.ObjectEffect import ObjectEffect

class ObjectEffectCreature(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._monsterFamilyIdFunc(input)
   
   def _monsterFamilyIdFunc(self,input) :
      self.monsterFamilyId = input.readVarUhShort()
      if(self.monsterFamilyId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.monsterFamilyId) + ") on element of ObjectEffectCreature.monsterFamilyId.")

   def resume(self):
      super().resume()
      print("monsterFamilyId :",self.monsterFamilyId)
