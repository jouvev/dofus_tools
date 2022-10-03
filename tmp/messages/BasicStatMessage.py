class BasicStatMessage:
   def __init__(self,input):
      self._timeSpentFunc(input)
      self._statIdFunc(input)
   
   def _timeSpentFunc(self,input) :
      self.timeSpent = input.readDouble()
      if(self.timeSpent < 0 or self.timeSpent > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.timeSpent + ") on element of BasicStatMessage.timeSpent.")
   
   def _statIdFunc(self,input) :
      self.statId = input.readVarUhShort()
      if(self.statId < 0) :
         raise RuntimeError("Forbidden value (" + self.statId + ") on element of BasicStatMessage.statId.")