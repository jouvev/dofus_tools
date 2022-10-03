from tmp.types.ObjectEffect import ObjectEffect
class ObjectEffectCreature(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._monsterFamilyIdFunc(input)
   
   def _monsterFamilyIdFunc(self,input) :
      self.monsterFamilyId = input.readVarUhShort()
      if(self.monsterFamilyId < 0) :
         raise RuntimeError("Forbidden value (" + self.monsterFamilyId + ") on element of ObjectEffectCreature.monsterFamilyId.")