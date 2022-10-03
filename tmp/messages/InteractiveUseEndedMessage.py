class InteractiveUseEndedMessage:
   def __init__(self,input):
      self._elemIdFunc(input)
      self._skillIdFunc(input)
   
   def _elemIdFunc(self,input) :
      self.elemId = input.readVarUhInt()
      if(self.elemId < 0) :
         raise RuntimeError("Forbidden value (" + self.elemId + ") on element of InteractiveUseEndedMessage.elemId.")
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhShort()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + self.skillId + ") on element of InteractiveUseEndedMessage.skillId.")