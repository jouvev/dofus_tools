class AccessoryPreviewRequestMessage:
   def __init__(self,input):
      self.genericId = []
      _val1 = 0
      _genericIdLen = input.readUnsignedShort()
      for _i1 in range(0,_genericIdLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of genericId.")
         self.genericId.append(_val1)

   def resume(self):
      print("genericId :",self.genericId)
