from tmp.types.SkillActionDescription import SkillActionDescription
class SkillActionDescriptionTimed(SkillActionDescription):
   def __init__(self,input):
      super().__init__(input)
      self._timeFunc(input)
   
   def _timeFunc(self,input) :
      self.time = input.readUnsignedByte()
      if(self.time < 0 or self.time > 255) :
         raise RuntimeError("Forbidden value (" + self.time + ") on element of SkillActionDescriptionTimed.time.")