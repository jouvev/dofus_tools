from tmp.types.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
class CharacterUsableCharacteristicDetailed(CharacterCharacteristicDetailed):
   def __init__(self,input):
      super().__init__(input)
      self._usedFunc(input)
   
   def _usedFunc(self,input) :
      self.used = input.readVarUhInt()
      if(self.used < 0) :
         raise RuntimeError("Forbidden value (" + self.used + ") on element of CharacterUsableCharacteristicDetailed.used.")