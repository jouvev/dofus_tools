class GameFightOptionStateUpdateMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._teamIdFunc(input)
      self._optionFunc(input)
      self._stateFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameFightOptionStateUpdateMessage.fightId.")
   
   def _teamIdFunc(self,input) :
      self.teamId = input.readByte()
      if(self.teamId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.teamId) + ") on element of GameFightOptionStateUpdateMessage.teamId.")
   
   def _optionFunc(self,input) :
      self.option = input.readByte()
      if(self.option < 0) :
         raise RuntimeError("Forbidden value (" + str(self.option) + ") on element of GameFightOptionStateUpdateMessage.option.")
   
   def _stateFunc(self,input) :
      self.state = input.readBoolean()

   def resume(self):
      print("fightId :",self.fightId)
      print("teamId :",self.teamId)
      print("option :",self.option)
      print("state :",self.state)
