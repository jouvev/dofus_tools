class GameRolePlayPlayerLifeStatusMessage:
   def __init__(self,input):
      self._stateFunc(input)
      self._phenixMapIdFunc(input)
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + self.state + ") on element of GameRolePlayPlayerLifeStatusMessage.state.")
   
   def _phenixMapIdFunc(self,input) :
      self.phenixMapId = input.readDouble()
      if(self.phenixMapId < 0 or self.phenixMapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.phenixMapId + ") on element of GameRolePlayPlayerLifeStatusMessage.phenixMapId.")