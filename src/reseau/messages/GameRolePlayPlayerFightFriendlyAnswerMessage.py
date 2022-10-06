class GameRolePlayPlayerFightFriendlyAnswerMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._acceptFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameRolePlayPlayerFightFriendlyAnswerMessage.fightId.")
   
   def _acceptFunc(self,input) :
      self.accept = input.readBoolean()

   def resume(self):
      print("fightId :",self.fightId)
      print("accept :",self.accept)
