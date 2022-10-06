from src.reseau.types.FightTeamMemberInformations import FightTeamMemberInformations

class FightTeamMemberEntityInformation(FightTeamMemberInformations):
   def __init__(self,input):
      super().__init__(input)
      self._entityModelIdFunc(input)
      self._levelFunc(input)
      self._masterIdFunc(input)
   
   def _entityModelIdFunc(self,input) :
      self.entityModelId = input.readByte()
      if(self.entityModelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.entityModelId) + ") on element of FightTeamMemberEntityInformation.entityModelId.")
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 1 or self.level > 200) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightTeamMemberEntityInformation.level.")
   
   def _masterIdFunc(self,input) :
      self.masterId = input.readDouble()
      if(self.masterId < -9007199254740992 or self.masterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element of FightTeamMemberEntityInformation.masterId.")

   def resume(self):
      super().resume()
      print("entityModelId :",self.entityModelId)
      print("level :",self.level)
      print("masterId :",self.masterId)
