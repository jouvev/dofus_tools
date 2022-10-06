from tmp.messages.ObjectUseMessage import ObjectUseMessage

class ObjectUseOnCharacterMessage(ObjectUseMessage):
   def __init__(self,input):
      super().__init__(input)
      self._characterIdFunc(input)
   
   def _characterIdFunc(self,input) :
      self.characterId = input.readVarUhLong()
      if(self.characterId < 0 or self.characterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.characterId) + ") on element of ObjectUseOnCharacterMessage.characterId.")

   def resume(self):
      super().resume()
      print("characterId :",self.characterId)
