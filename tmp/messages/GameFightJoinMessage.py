class GameFightJoinMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._timeMaxBeforeFightStartFunc(input)
      self._fightTypeFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.isTeamPhase = bool(bin(_box0)[2:].zfill(8)[0])
      self.canBeCancelled = bool(bin(_box0)[2:].zfill(8)[1])
      self.canSayReady = bool(bin(_box0)[2:].zfill(8)[2])
      self.isFightStarted = bool(bin(_box0)[2:].zfill(8)[3])
   
   def _timeMaxBeforeFightStartFunc(self,input) :
      self.timeMaxBeforeFightStart = input.readShort()
      if(self.timeMaxBeforeFightStart < 0) :
         raise RuntimeError("Forbidden value (" + self.timeMaxBeforeFightStart + ") on element of GameFightJoinMessage.timeMaxBeforeFightStart.")
   
   def _fightTypeFunc(self,input) :
      self.fightType = input.readByte()
      if(self.fightType < 0) :
         raise RuntimeError("Forbidden value (" + self.fightType + ") on element of GameFightJoinMessage.fightType.")