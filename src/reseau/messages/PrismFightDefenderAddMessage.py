class PrismFightDefenderAddMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._fightIdFunc(input)
      _id3 = input.readUnsignedShort()
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismFightDefenderAddMessage.subAreaId.")
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of PrismFightDefenderAddMessage.fightId.")

   def resume(self):
      print("subAreaId :",self.subAreaId)
      print("fightId :",self.fightId)
