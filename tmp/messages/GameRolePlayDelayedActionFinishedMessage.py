class GameRolePlayDelayedActionFinishedMessage:
   def __init__(self,input):
      self._delayedCharacterIdFunc(input)
      self._delayTypeIdFunc(input)
   
   def _delayedCharacterIdFunc(self,input) :
      self.delayedCharacterId = input.readDouble()
      if(self.delayedCharacterId < -9007199254740992 or self.delayedCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.delayedCharacterId + ") on element of GameRolePlayDelayedActionFinishedMessage.delayedCharacterId.")
   
   def _delayTypeIdFunc(self,input) :
      self.delayTypeId = input.readByte()
      if(self.delayTypeId < 0) :
         raise RuntimeError("Forbidden value (" + self.delayTypeId + ") on element of GameRolePlayDelayedActionFinishedMessage.delayTypeId.")