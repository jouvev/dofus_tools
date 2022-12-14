class BreachRewardBoughtMessage:
   def __init__(self,input):
      self._idFunc(input)
      self._boughtFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of BreachRewardBoughtMessage.id.")
   
   def _boughtFunc(self,input) :
      self.bought = input.readBoolean()

   def resume(self):
      print("id :",self.id)
      print("bought :",self.bought)
