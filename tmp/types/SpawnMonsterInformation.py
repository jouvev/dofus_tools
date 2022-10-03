from tmp.types.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation
class SpawnMonsterInformation(BaseSpawnMonsterInformation):
   def __init__(self,input):
      super().__init__(input)
      self._creatureGradeFunc(input)
   
   def _creatureGradeFunc(self,input) :
      self.creatureGrade = input.readByte()
      if(self.creatureGrade < 0) :
         raise RuntimeError("Forbidden value (" + self.creatureGrade + ") on element of SpawnMonsterInformation.creatureGrade.")