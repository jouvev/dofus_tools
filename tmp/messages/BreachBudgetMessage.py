class BreachBudgetMessage:
   def __init__(self,input):
      self._bugdetFunc(input)
   
   def _bugdetFunc(self,input) :
      self.bugdet = input.readVarUhInt()
      if(self.bugdet < 0) :
         raise RuntimeError("Forbidden value (" + str(self.bugdet) + ") on element of BreachBudgetMessage.bugdet.")

   def resume(self):
      print("bugdet :",self.bugdet)
