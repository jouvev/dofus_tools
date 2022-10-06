from src.reseau.messages.AbstractPartyEventMessage import AbstractPartyEventMessage

class PartyUpdateLightMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      self._idFunc(input)
      self._lifePointsFunc(input)
      self._maxLifePointsFunc(input)
      self._prospectingFunc(input)
      self._regenRateFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhLong()
      if(self.id < 0 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of PartyUpdateLightMessage.id.")
   
   def _lifePointsFunc(self,input) :
      self.lifePoints = input.readVarUhInt()
      if(self.lifePoints < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element of PartyUpdateLightMessage.lifePoints.")
   
   def _maxLifePointsFunc(self,input) :
      self.maxLifePoints = input.readVarUhInt()
      if(self.maxLifePoints < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element of PartyUpdateLightMessage.maxLifePoints.")
   
   def _prospectingFunc(self,input) :
      self.prospecting = input.readVarUhInt()
      if(self.prospecting < 0) :
         raise RuntimeError("Forbidden value (" + str(self.prospecting) + ") on element of PartyUpdateLightMessage.prospecting.")
   
   def _regenRateFunc(self,input) :
      self.regenRate = input.readUnsignedByte()
      if(self.regenRate < 0 or self.regenRate > 255) :
         raise RuntimeError("Forbidden value (" + str(self.regenRate) + ") on element of PartyUpdateLightMessage.regenRate.")

   def resume(self):
      super().resume()
      print("id :",self.id)
      print("lifePoints :",self.lifePoints)
      print("maxLifePoints :",self.maxLifePoints)
      print("prospecting :",self.prospecting)
      print("regenRate :",self.regenRate)
