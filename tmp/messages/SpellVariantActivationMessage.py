class SpellVariantActivationMessage:
   def __init__(self,input):
      self._spellIdFunc(input)
      self._resultFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + self.spellId + ") on element of SpellVariantActivationMessage.spellId.")
   
   def _resultFunc(self,input) :
      self.result = input.readBoolean()