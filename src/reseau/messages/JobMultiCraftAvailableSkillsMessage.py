from src.reseau.messages.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage

class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
   def __init__(self,input):
      self.skills = []
      _val2 = 0
      super().__init__(input)
      self._playerIdFunc(input)
      _skillsLen = input.readUnsignedShort()
      for _i2 in range(0,_skillsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of skills.")
         self.skills.append(_val2)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of JobMultiCraftAvailableSkillsMessage.playerId.")

   def resume(self):
      super().resume()
      print("playerId :",self.playerId)
      print("skills :",self.skills)
