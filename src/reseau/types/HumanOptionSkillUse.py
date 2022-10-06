from src.reseau.types.HumanOption import HumanOption

class HumanOptionSkillUse(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self._elementIdFunc(input)
      self._skillIdFunc(input)
      self._skillEndTimeFunc(input)
   
   def _elementIdFunc(self,input) :
      self.elementId = input.readVarUhInt()
      if(self.elementId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element of HumanOptionSkillUse.elementId.")
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhShort()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of HumanOptionSkillUse.skillId.")
   
   def _skillEndTimeFunc(self,input) :
      self.skillEndTime = input.readDouble()
      if(self.skillEndTime < -9007199254740992 or self.skillEndTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.skillEndTime) + ") on element of HumanOptionSkillUse.skillEndTime.")

   def resume(self):
      super().resume()
      print("elementId :",self.elementId)
      print("skillId :",self.skillId)
      print("skillEndTime :",self.skillEndTime)
