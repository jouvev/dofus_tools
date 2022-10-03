from tmp.types.SpellItem import SpellItem
class ForgettableSpellItem(SpellItem):
   def __init__(self,input):
      super().__init__(input)
      self._availableFunc(input)
   
   def _availableFunc(self,input) :
      self.available = input.readBoolean()