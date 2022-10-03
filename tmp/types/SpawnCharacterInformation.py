from tmp.types.SpawnInformation import SpawnInformation
class SpawnCharacterInformation(SpawnInformation):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
      self._levelFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 1 or self.level > 200) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of SpawnCharacterInformation.level.")