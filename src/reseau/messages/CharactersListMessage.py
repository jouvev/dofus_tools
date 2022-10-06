from src.reseau.messages.BasicCharactersListMessage import BasicCharactersListMessage

class CharactersListMessage(BasicCharactersListMessage):
   def __init__(self,input):
      super().__init__(input)
      self._hasStartupActionsFunc(input)
   
   def _hasStartupActionsFunc(self,input) :
      self.hasStartupActions = input.readBoolean()

   def resume(self):
      super().resume()
      print("hasStartupActions :",self.hasStartupActions)
