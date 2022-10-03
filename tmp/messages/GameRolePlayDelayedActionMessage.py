class GameRolePlayDelayedActionMessage:
   def __init__(self,input):
      self._delayedCharacterIdFunc(input)
      self._delayTypeIdFunc(input)
      self._delayEndTimeFunc(input)
   
   def _delayedCharacterIdFunc(self,input) :
      self.delayedCharacterId = input.readDouble()
      if(self.delayedCharacterId < -9007199254740992 or self.delayedCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.delayedCharacterId + ") on element of GameRolePlayDelayedActionMessage.delayedCharacterId.")
   
   def _delayTypeIdFunc(self,input) :
      self.delayTypeId = input.readByte()
      if(self.delayTypeId < 0) :
         raise RuntimeError("Forbidden value (" + self.delayTypeId + ") on element of GameRolePlayDelayedActionMessage.delayTypeId.")
   
   def _delayEndTimeFunc(self,input) :
      self.delayEndTime = input.readDouble()
      if(self.delayEndTime < 0 or self.delayEndTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.delayEndTime + ") on element of GameRolePlayDelayedActionMessage.delayEndTime.")