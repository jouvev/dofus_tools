class DecraftedItemStackInfo:
   def __init__(self,input):
      self.runesId = []
      self.runesQty = []
      _val4 = 0
      _val5 = 0
      self._objectUIDFunc(input)
      self._bonusMinFunc(input)
      self._bonusMaxFunc(input)
      _runesIdLen = input.readUnsignedShort()
      for _i4 in range(0,_runesIdLen):
         _val4 = input.readVarUhInt()
         if(_val4 < 0) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of runesId.")
         self.runesId.append(_val4)
      _runesQtyLen = input.readUnsignedShort()
      for _i5 in range(0,_runesQtyLen):
         _val5 = input.readVarUhInt()
         if(_val5 < 0) :
            raise RuntimeError("Forbidden value (" + _val5 + ") on elements of runesQty.")
         self.runesQty.append(_val5)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of DecraftedItemStackInfo.objectUID.")
   
   def _bonusMinFunc(self,input) :
      self.bonusMin = input.readFloat()
   
   def _bonusMaxFunc(self,input) :
      self.bonusMax = input.readFloat()

   def resume(self):
      print("objectUID :",self.objectUID)
      print("bonusMin :",self.bonusMin)
      print("bonusMax :",self.bonusMax)
      print("runesId :",self.runesId)
      print("runesQty :",self.runesQty)
