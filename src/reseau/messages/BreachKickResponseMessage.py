from src.reseau.types.CharacterMinimalInformations import CharacterMinimalInformations

class BreachKickResponseMessage:
   def __init__(self,input):
      self.target = CharacterMinimalInformations(input)
      self._kickedFunc(input)
   
   def _kickedFunc(self,input) :
      self.kicked = input.readBoolean()

   def resume(self):
      print("kicked :",self.kicked)
      self.target.resum()
