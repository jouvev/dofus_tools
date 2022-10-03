class ItemForPreset:
   def __init__(self,input):
      self._positionFunc(input)
      self._objGidFunc(input)
      self._objUidFunc(input)
   
   def _positionFunc(self,input) :
      self.position = input.readShort()
      if(self.position < 0) :
         raise RuntimeError("Forbidden value (" + self.position + ") on element of ItemForPreset.position.")
   
   def _objGidFunc(self,input) :
      self.objGid = input.readVarUhInt()
      if(self.objGid < 0) :
         raise RuntimeError("Forbidden value (" + self.objGid + ") on element of ItemForPreset.objGid.")
   
   def _objUidFunc(self,input) :
      self.objUid = input.readVarUhInt()
      if(self.objUid < 0) :
         raise RuntimeError("Forbidden value (" + self.objUid + ") on element of ItemForPreset.objUid.")