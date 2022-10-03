from tmp.types.CharacterBaseInformations import CharacterBaseInformations
class CharacterHardcoreOrEpicInformations(CharacterBaseInformations):
   def __init__(self,input):
      super().__init__(input)
      self._deathStateFunc(input)
      self._deathCountFunc(input)
      self._deathMaxLevelFunc(input)
   
   def _deathStateFunc(self,input) :
      self.deathState = input.readByte()
      if(self.deathState < 0) :
         raise RuntimeError("Forbidden value (" + self.deathState + ") on element of CharacterHardcoreOrEpicInformations.deathState.")
   
   def _deathCountFunc(self,input) :
      self.deathCount = input.readVarUhShort()
      if(self.deathCount < 0) :
         raise RuntimeError("Forbidden value (" + self.deathCount + ") on element of CharacterHardcoreOrEpicInformations.deathCount.")
   
   def _deathMaxLevelFunc(self,input) :
      self.deathMaxLevel = input.readVarUhShort()
      if(self.deathMaxLevel < 0) :
         raise RuntimeError("Forbidden value (" + self.deathMaxLevel + ") on element of CharacterHardcoreOrEpicInformations.deathMaxLevel.")