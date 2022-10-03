from tmp.types.SkillActionDescription import SkillActionDescription
class SkillActionDescriptionCraft(SkillActionDescription):
   def __init__(self,input):
      super().__init__(input)
      self._probabilityFunc(input)
   
   def _probabilityFunc(self,input) :
      self.probability = input.readByte()
      if(self.probability < 0) :
         raise RuntimeError("Forbidden value (" + self.probability + ") on element of SkillActionDescriptionCraft.probability.")