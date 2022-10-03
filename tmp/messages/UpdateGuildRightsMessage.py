class UpdateGuildRightsMessage:
   def __init__(self,input):
      self.rights = []
      _val2 = 0
      self._rankIdFunc(input)
      _rightsLen = input.readUnsignedShort()
      for _i2 in range(0,_rightsLen):
         _val2 = input.readVarUhInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of rights.")
         self.rights.append(_val2)
   
   def _rankIdFunc(self,input) :
      self.rankId = input.readVarUhInt()
      if(self.rankId < 0) :
         raise RuntimeError("Forbidden value (" + self.rankId + ") on element of UpdateGuildRightsMessage.rankId.")