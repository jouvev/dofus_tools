class SkillActionDescription:
   def __init__(self,input):
      self._skillIdFunc(input)
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhShort()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of SkillActionDescription.skillId.")

   def resume(self):
      print("skillId :",self.skillId)
