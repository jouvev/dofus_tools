class ObjectGroundAddedMessage:
   def __init__(self,input):
      self._cellIdFunc(input)
      self._objectGIDFunc(input)
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readVarUhShort()
      if(self.cellId < 0 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + self.cellId + ") on element of ObjectGroundAddedMessage.cellId.")
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectGID + ") on element of ObjectGroundAddedMessage.objectGID.")