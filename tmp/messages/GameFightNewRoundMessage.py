class GameFightNewRoundMessage:
   def __init__(self,input):
      self._roundNumberFunc(input)
   
   def _roundNumberFunc(self,input) :
      self.roundNumber = input.readVarUhInt()
      if(self.roundNumber < 0) :
         raise RuntimeError("Forbidden value (" + str(self.roundNumber) + ") on element of GameFightNewRoundMessage.roundNumber.")

   def resume(self):
      print("roundNumber :",self.roundNumber)
