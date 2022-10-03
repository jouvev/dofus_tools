class UpdatedStorageTabInformation:
   def __init__(self,input):
      self.dropTypeLimitation = []
      _val4 = 0
      self._nameFunc(input)
      self._tabNumberFunc(input)
      self._pictoFunc(input)
      _dropTypeLimitationLen = input.readUnsignedShort()
      for _i4 in range(0,_dropTypeLimitationLen):
         _val4 = input.readVarUhInt()
         if(_val4 < 0) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of dropTypeLimitation.")
         self.dropTypeLimitation.append(_val4)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _tabNumberFunc(self,input) :
      self.tabNumber = input.readVarUhInt()
      if(self.tabNumber < 0) :
         raise RuntimeError("Forbidden value (" + self.tabNumber + ") on element of UpdatedStorageTabInformation.tabNumber.")
   
   def _pictoFunc(self,input) :
      self.picto = input.readVarUhInt()
      if(self.picto < 0) :
         raise RuntimeError("Forbidden value (" + self.picto + ") on element of UpdatedStorageTabInformation.picto.")