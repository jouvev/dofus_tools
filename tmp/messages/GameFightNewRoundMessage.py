class GameFightNewRoundMessage:
   def __init__(self,input):
      self._roundNumberFunc(input)
   
   def _roundNumberFunc(self,input) :
      self.roundNumber = input.readVarUhInt()
      if(self.roundNumber < 0) :
         raise RuntimeError("Forbidden value (" + self.roundNumber + ") on element of GameFightNewRoundMessage.roundNumber.")