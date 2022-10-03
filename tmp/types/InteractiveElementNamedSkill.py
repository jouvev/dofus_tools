from tmp.types.InteractiveElementSkill import InteractiveElementSkill
class InteractiveElementNamedSkill(InteractiveElementSkill):
   def __init__(self,input):
      super().__init__(input)
      self._nameIdFunc(input)
   
   def _nameIdFunc(self,input) :
      self.nameId = input.readVarUhInt()
      if(self.nameId < 0) :
         raise RuntimeError("Forbidden value (" + self.nameId + ") on element of InteractiveElementNamedSkill.nameId.")