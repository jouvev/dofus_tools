from src.reseau.types.CharacterRemodelingInformation import CharacterRemodelingInformation

class CharacterToRemodelInformations(CharacterRemodelingInformation):
   def __init__(self,input):
      super().__init__(input)
      self._possibleChangeMaskFunc(input)
      self._mandatoryChangeMaskFunc(input)
   
   def _possibleChangeMaskFunc(self,input) :
      self.possibleChangeMask = input.readByte()
      if(self.possibleChangeMask < 0) :
         raise RuntimeError("Forbidden value (" + str(self.possibleChangeMask) + ") on element of CharacterToRemodelInformations.possibleChangeMask.")
   
   def _mandatoryChangeMaskFunc(self,input) :
      self.mandatoryChangeMask = input.readByte()
      if(self.mandatoryChangeMask < 0) :
         raise RuntimeError("Forbidden value (" + str(self.mandatoryChangeMask) + ") on element of CharacterToRemodelInformations.mandatoryChangeMask.")

   def resume(self):
      super().resume()
      print("possibleChangeMask :",self.possibleChangeMask)
      print("mandatoryChangeMask :",self.mandatoryChangeMask)
