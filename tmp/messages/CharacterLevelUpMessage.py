class CharacterLevelUpMessage:
   def __init__(self,input):
      self._newLevelFunc(input)
   
   def _newLevelFunc(self,input) :
      self.newLevel = input.readVarUhShort()
      if(self.newLevel < 0) :
         raise RuntimeError("Forbidden value (" + self.newLevel + ") on element of CharacterLevelUpMessage.newLevel.")