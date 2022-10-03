class PrismFightDefenderLeaveMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._fightIdFunc(input)
      self._fighterToRemoveIdFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PrismFightDefenderLeaveMessage.subAreaId.")
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + self.fightId + ") on element of PrismFightDefenderLeaveMessage.fightId.")
   
   def _fighterToRemoveIdFunc(self,input) :
      self.fighterToRemoveId = input.readVarUhLong()
      if(self.fighterToRemoveId < 0 or self.fighterToRemoveId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.fighterToRemoveId + ") on element of PrismFightDefenderLeaveMessage.fighterToRemoveId.")