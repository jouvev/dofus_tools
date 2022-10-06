from src.reseau.types.SkillActionDescription import SkillActionDescription

class SkillActionDescriptionCraft(SkillActionDescription):
   def __init__(self,input):
      super().__init__(input)
      self._probabilityFunc(input)
   
   def _probabilityFunc(self,input) :
      self.probability = input.readByte()
      if(self.probability < 0) :
         raise RuntimeError("Forbidden value (" + str(self.probability) + ") on element of SkillActionDescriptionCraft.probability.")

   def resume(self):
      super().resume()
      print("probability :",self.probability)
