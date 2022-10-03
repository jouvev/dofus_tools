class InteractiveUseRequestMessage:
   def __init__(self,input):
      self._elemIdFunc(input)
      self._skillInstanceUidFunc(input)
   
   def _elemIdFunc(self,input) :
      self.elemId = input.readVarUhInt()
      if(self.elemId < 0) :
         raise RuntimeError("Forbidden value (" + self.elemId + ") on element of InteractiveUseRequestMessage.elemId.")
   
   def _skillInstanceUidFunc(self,input) :
      self.skillInstanceUid = input.readVarUhInt()
      if(self.skillInstanceUid < 0) :
         raise RuntimeError("Forbidden value (" + self.skillInstanceUid + ") on element of InteractiveUseRequestMessage.skillInstanceUid.")