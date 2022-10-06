from src.reseau.types.Item import Item

class SpellItem(Item):
   def __init__(self,input):
      super().__init__(input)
      self._spellIdFunc(input)
      self._spellLevelFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readInt()
   
   def _spellLevelFunc(self,input) :
      self.spellLevel = input.readShort()
      if(self.spellLevel < 1 or self.spellLevel > 32767) :
         raise RuntimeError("Forbidden value (" + str(self.spellLevel) + ") on element of SpellItem.spellLevel.")

   def resume(self):
      super().resume()
      print("spellId :",self.spellId)
      print("spellLevel :",self.spellLevel)
