class GameFightJoinRequestMessage:
   def __init__(self,input):
      self._fighterIdFunc(input)
      self._fightIdFunc(input)
   
   def _fighterIdFunc(self,input) :
      self.fighterId = input.readDouble()
      if(self.fighterId < -9007199254740992 or self.fighterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.fighterId) + ") on element of GameFightJoinRequestMessage.fighterId.")
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameFightJoinRequestMessage.fightId.")

   def resume(self):
      print("fighterId :",self.fighterId)
      print("fightId :",self.fightId)
