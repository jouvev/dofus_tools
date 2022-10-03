from tmp.types.SkillActionDescriptionTimed import SkillActionDescriptionTimed
class SkillActionDescriptionCollect(SkillActionDescriptionTimed):
   def __init__(self,input):
      super().__init__(input)
      self._minFunc(input)
      self._maxFunc(input)
   
   def _minFunc(self,input) :
      self.min = input.readVarUhShort()
      if(self.min < 0) :
         raise RuntimeError("Forbidden value (" + self.min + ") on element of SkillActionDescriptionCollect.min.")
   
   def _maxFunc(self,input) :
      self.max = input.readVarUhShort()
      if(self.max < 0) :
         raise RuntimeError("Forbidden value (" + self.max + ") on element of SkillActionDescriptionCollect.max.")