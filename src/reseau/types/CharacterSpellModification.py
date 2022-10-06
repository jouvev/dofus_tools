from src.reseau.types.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed

class CharacterSpellModification:
   def __init__(self,input):
      self._modificationTypeFunc(input)
      self._spellIdFunc(input)
      self.value = CharacterCharacteristicDetailed(input)
   
   def _modificationTypeFunc(self,input) :
      self.modificationType = input.readByte()
      if(self.modificationType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.modificationType) + ") on element of CharacterSpellModification.modificationType.")
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of CharacterSpellModification.spellId.")

   def resume(self):
      print("modificationType :",self.modificationType)
      print("spellId :",self.spellId)
      self.value.resum()
