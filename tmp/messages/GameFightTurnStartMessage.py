class GameFightTurnStartMessage:
   def __init__(self,input):
      self._idFunc(input)
      self._waitTimeFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < -9007199254740992 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of GameFightTurnStartMessage.id.")
   
   def _waitTimeFunc(self,input) :
      self.waitTime = input.readVarUhInt()
      if(self.waitTime < 0) :
         raise RuntimeError("Forbidden value (" + str(self.waitTime) + ") on element of GameFightTurnStartMessage.waitTime.")

   def resume(self):
      print("id :",self.id)
      print("waitTime :",self.waitTime)
