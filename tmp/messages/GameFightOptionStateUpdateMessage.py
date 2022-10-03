class GameFightOptionStateUpdateMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._teamIdFunc(input)
      self._optionFunc(input)
      self._stateFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + self.fightId + ") on element of GameFightOptionStateUpdateMessage.fightId.")
   
   def _teamIdFunc(self,input) :
      self.teamId = input.readByte()
      if(self.teamId < 0) :
         raise RuntimeError("Forbidden value (" + self.teamId + ") on element of GameFightOptionStateUpdateMessage.teamId.")
   
   def _optionFunc(self,input) :
      self.option = input.readByte()
      if(self.option < 0) :
         raise RuntimeError("Forbidden value (" + self.option + ") on element of GameFightOptionStateUpdateMessage.option.")
   
   def _stateFunc(self,input) :
      self.state = input.readBoolean()