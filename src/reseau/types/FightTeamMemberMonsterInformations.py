from src.reseau.types.FightTeamMemberInformations import FightTeamMemberInformations

class FightTeamMemberMonsterInformations(FightTeamMemberInformations):
   def __init__(self,input):
      super().__init__(input)
      self._monsterIdFunc(input)
      self._gradeFunc(input)
   
   def _monsterIdFunc(self,input) :
      self.monsterId = input.readInt()
   
   def _gradeFunc(self,input) :
      self.grade = input.readByte()
      if(self.grade < 0) :
         raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element of FightTeamMemberMonsterInformations.grade.")

   def resume(self):
      super().resume()
      print("monsterId :",self.monsterId)
      print("grade :",self.grade)
