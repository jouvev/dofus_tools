class CharacterDeletionRequestMessage:
   def __init__(self,input):
      self._characterIdFunc(input)
      self._secretAnswerHashFunc(input)
   
   def _characterIdFunc(self,input) :
      self.characterId = input.readVarUhLong()
      if(self.characterId < 0 or self.characterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.characterId + ") on element of CharacterDeletionRequestMessage.characterId.")
   
   def _secretAnswerHashFunc(self,input) :
      self.secretAnswerHash = input.readUTF()