class StorageTabInformation:
   def __init__(self,input):
      self.dropTypeLimitation = []
      _val7 = 0
      self._nameFunc(input)
      self._tabNumberFunc(input)
      self._pictoFunc(input)
      self._openRightFunc(input)
      self._dropRightFunc(input)
      self._takeRightFunc(input)
      _dropTypeLimitationLen = input.readUnsignedShort()
      for _i7 in range(0,_dropTypeLimitationLen):
         _val7 = input.readVarUhInt()
         if(_val7 < 0) :
            raise RuntimeError("Forbidden value (" + _val7 + ") on elements of dropTypeLimitation.")
         self.dropTypeLimitation.append(_val7)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _tabNumberFunc(self,input) :
      self.tabNumber = input.readVarUhInt()
      if(self.tabNumber < 0) :
         raise RuntimeError("Forbidden value (" + self.tabNumber + ") on element of StorageTabInformation.tabNumber.")
   
   def _pictoFunc(self,input) :
      self.picto = input.readVarUhInt()
      if(self.picto < 0) :
         raise RuntimeError("Forbidden value (" + self.picto + ") on element of StorageTabInformation.picto.")
   
   def _openRightFunc(self,input) :
      self.openRight = input.readVarUhInt()
      if(self.openRight < 0) :
         raise RuntimeError("Forbidden value (" + self.openRight + ") on element of StorageTabInformation.openRight.")
   
   def _dropRightFunc(self,input) :
      self.dropRight = input.readVarUhInt()
      if(self.dropRight < 0) :
         raise RuntimeError("Forbidden value (" + self.dropRight + ") on element of StorageTabInformation.dropRight.")
   
   def _takeRightFunc(self,input) :
      self.takeRight = input.readVarUhInt()
      if(self.takeRight < 0) :
         raise RuntimeError("Forbidden value (" + self.takeRight + ") on element of StorageTabInformation.takeRight.")