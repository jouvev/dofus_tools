from src.reseau.types.ObjectEffectCreature import ObjectEffectCreature

class ObjectEffectLadder(ObjectEffectCreature):
   def __init__(self,input):
      super().__init__(input)
      self._monsterCountFunc(input)
   
   def _monsterCountFunc(self,input) :
      self.monsterCount = input.readVarUhInt()
      if(self.monsterCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.monsterCount) + ") on element of ObjectEffectLadder.monsterCount.")

   def resume(self):
      super().resume()
      print("monsterCount :",self.monsterCount)
