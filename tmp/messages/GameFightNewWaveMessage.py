class GameFightNewWaveMessage:
   def __init__(self,input):
      self._idFunc(input)
      self._teamIdFunc(input)
      self._nbTurnBeforeNextWaveFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readByte()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of GameFightNewWaveMessage.id.")
   
   def _teamIdFunc(self,input) :
      self.teamId = input.readByte()
      if(self.teamId < 0) :
         raise RuntimeError("Forbidden value (" + self.teamId + ") on element of GameFightNewWaveMessage.teamId.")
   
   def _nbTurnBeforeNextWaveFunc(self,input) :
      self.nbTurnBeforeNextWave = input.readShort()