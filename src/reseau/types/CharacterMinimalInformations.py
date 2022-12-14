from src.reseau.types.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations

class CharacterMinimalInformations(CharacterBasicMinimalInformations):
   def __init__(self,input):
      super().__init__(input)
      self._levelFunc(input)
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of CharacterMinimalInformations.level.")

   def resume(self):
      super().resume()
      print("level :",self.level)
