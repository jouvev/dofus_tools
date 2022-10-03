class CharacterReplayRequestMessage:
   def __init__(self,input):
      self._characterIdFunc(input)
   
   def _characterIdFunc(self,input) :
      self.characterId = input.readVarUhLong()
      if(self.characterId < 0 or self.characterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.characterId + ") on element of CharacterReplayRequestMessage.characterId.")