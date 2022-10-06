class PrismFightAttackerRemoveMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._fightIdFunc(input)
      self._fighterToRemoveIdFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismFightAttackerRemoveMessage.subAreaId.")
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of PrismFightAttackerRemoveMessage.fightId.")
   
   def _fighterToRemoveIdFunc(self,input) :
      self.fighterToRemoveId = input.readVarUhLong()
      if(self.fighterToRemoveId < 0 or self.fighterToRemoveId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.fighterToRemoveId) + ") on element of PrismFightAttackerRemoveMessage.fighterToRemoveId.")

   def resume(self):
      print("subAreaId :",self.subAreaId)
      print("fightId :",self.fightId)
      print("fighterToRemoveId :",self.fighterToRemoveId)
