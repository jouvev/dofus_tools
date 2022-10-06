class BreachRewardBuyMessage:
   def __init__(self,input):
      self._idFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of BreachRewardBuyMessage.id.")

   def resume(self):
      print("id :",self.id)
