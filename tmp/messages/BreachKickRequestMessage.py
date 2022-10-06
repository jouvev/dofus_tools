class BreachKickRequestMessage:
   def __init__(self,input):
      self._targetFunc(input)
   
   def _targetFunc(self,input) :
      self.target = input.readVarUhLong()
      if(self.target < 0 or self.target > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.target) + ") on element of BreachKickRequestMessage.target.")

   def resume(self):
      print("target :",self.target)
