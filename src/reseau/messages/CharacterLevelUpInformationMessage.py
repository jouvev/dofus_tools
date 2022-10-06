from src.reseau.messages.CharacterLevelUpMessage import CharacterLevelUpMessage

class CharacterLevelUpInformationMessage(CharacterLevelUpMessage):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
      self._idFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _idFunc(self,input) :
      self.id = input.readVarUhLong()
      if(self.id < 0 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of CharacterLevelUpInformationMessage.id.")

   def resume(self):
      super().resume()
      print("name :",self.name)
      print("id :",self.id)
