class CharacterDeletionPrepareMessage:
   def __init__(self,input):
      self._characterIdFunc(input)
      self._characterNameFunc(input)
      self._secretQuestionFunc(input)
      self._needSecretAnswerFunc(input)
   
   def _characterIdFunc(self,input) :
      self.characterId = input.readVarUhLong()
      if(self.characterId < 0 or self.characterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.characterId) + ") on element of CharacterDeletionPrepareMessage.characterId.")
   
   def _characterNameFunc(self,input) :
      self.characterName = input.readUTF()
   
   def _secretQuestionFunc(self,input) :
      self.secretQuestion = input.readUTF()
   
   def _needSecretAnswerFunc(self,input) :
      self.needSecretAnswer = input.readBoolean()

   def resume(self):
      print("characterId :",self.characterId)
      print("characterName :",self.characterName)
      print("secretQuestion :",self.secretQuestion)
      print("needSecretAnswer :",self.needSecretAnswer)
