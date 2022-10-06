class ItemForPreset:
   def __init__(self,input):
      self._positionFunc(input)
      self._objGidFunc(input)
      self._objUidFunc(input)
   
   def _positionFunc(self,input) :
      self.position = input.readShort()
      if(self.position < 0) :
         raise RuntimeError("Forbidden value (" + str(self.position) + ") on element of ItemForPreset.position.")
   
   def _objGidFunc(self,input) :
      self.objGid = input.readVarUhInt()
      if(self.objGid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objGid) + ") on element of ItemForPreset.objGid.")
   
   def _objUidFunc(self,input) :
      self.objUid = input.readVarUhInt()
      if(self.objUid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objUid) + ") on element of ItemForPreset.objUid.")

   def resume(self):
      print("position :",self.position)
      print("objGid :",self.objGid)
      print("objUid :",self.objUid)
