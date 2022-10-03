from tmp.types.PartyEntityBaseInformation import PartyEntityBaseInformation
class PartyEntityMemberInformation(PartyEntityBaseInformation):
   def __init__(self,input):
      super().__init__(input)
      self._initiativeFunc(input)
      self._lifePointsFunc(input)
      self._maxLifePointsFunc(input)
      self._prospectingFunc(input)
      self._regenRateFunc(input)
   
   def _initiativeFunc(self,input) :
      self.initiative = input.readVarUhInt()
      if(self.initiative < 0) :
         raise RuntimeError("Forbidden value (" + self.initiative + ") on element of PartyEntityMemberInformation.initiative.")
   
   def _lifePointsFunc(self,input) :
      self.lifePoints = input.readVarUhInt()
      if(self.lifePoints < 0) :
         raise RuntimeError("Forbidden value (" + self.lifePoints + ") on element of PartyEntityMemberInformation.lifePoints.")
   
   def _maxLifePointsFunc(self,input) :
      self.maxLifePoints = input.readVarUhInt()
      if(self.maxLifePoints < 0) :
         raise RuntimeError("Forbidden value (" + self.maxLifePoints + ") on element of PartyEntityMemberInformation.maxLifePoints.")
   
   def _prospectingFunc(self,input) :
      self.prospecting = input.readVarUhInt()
      if(self.prospecting < 0) :
         raise RuntimeError("Forbidden value (" + self.prospecting + ") on element of PartyEntityMemberInformation.prospecting.")
   
   def _regenRateFunc(self,input) :
      self.regenRate = input.readUnsignedByte()
      if(self.regenRate < 0 or self.regenRate > 255) :
         raise RuntimeError("Forbidden value (" + self.regenRate + ") on element of PartyEntityMemberInformation.regenRate.")