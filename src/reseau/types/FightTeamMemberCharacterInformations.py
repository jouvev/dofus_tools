from src.reseau.types.FightTeamMemberInformations import FightTeamMemberInformations

class FightTeamMemberCharacterInformations(FightTeamMemberInformations):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
      self._levelFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightTeamMemberCharacterInformations.level.")

   def resume(self):
      super().resume()
      print("name :",self.name)
      print("level :",self.level)
