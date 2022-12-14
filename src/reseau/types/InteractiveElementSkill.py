class InteractiveElementSkill:
   def __init__(self,input):
      self._skillIdFunc(input)
      self._skillInstanceUidFunc(input)
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhInt()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of InteractiveElementSkill.skillId.")
   
   def _skillInstanceUidFunc(self,input) :
      self.skillInstanceUid = input.readInt()
      if(self.skillInstanceUid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillInstanceUid) + ") on element of InteractiveElementSkill.skillInstanceUid.")

   def resume(self):
      print("skillId :",self.skillId)
      print("skillInstanceUid :",self.skillInstanceUid)
