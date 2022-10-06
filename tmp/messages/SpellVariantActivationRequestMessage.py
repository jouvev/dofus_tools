class SpellVariantActivationRequestMessage:
   def __init__(self,input):
      self._spellIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of SpellVariantActivationRequestMessage.spellId.")

   def resume(self):
      print("spellId :",self.spellId)
