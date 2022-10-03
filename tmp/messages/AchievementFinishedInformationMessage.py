from tmp.messages.AchievementFinishedMessage import AchievementFinishedMessage
class AchievementFinishedInformationMessage(AchievementFinishedMessage):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
      self._playerIdFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of AchievementFinishedInformationMessage.playerId.")