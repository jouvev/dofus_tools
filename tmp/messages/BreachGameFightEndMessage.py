from tmp.messages.GameFightEndMessage import GameFightEndMessage

class BreachGameFightEndMessage(GameFightEndMessage):
   def __init__(self,input):
      super().__init__(input)
      self._budgetFunc(input)
   
   def _budgetFunc(self,input) :
      self.budget = input.readInt()

   def resume(self):
      super().resume()
      print("budget :",self.budget)
