from src.reseau.types.InteractiveElementSkill import InteractiveElementSkill

class InteractiveElementNamedSkill(InteractiveElementSkill):
   def __init__(self,input):
      super().__init__(input)
      self._nameIdFunc(input)
   
   def _nameIdFunc(self,input) :
      self.nameId = input.readVarUhInt()
      if(self.nameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nameId) + ") on element of InteractiveElementNamedSkill.nameId.")

   def resume(self):
      super().resume()
      print("nameId :",self.nameId)
