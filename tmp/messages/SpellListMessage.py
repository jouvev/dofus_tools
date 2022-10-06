from tmp.types.SpellItem import SpellItem

class SpellListMessage:
   def __init__(self,input):
      self.spells = []
      _item2 = None
      self._spellPrevisualizationFunc(input)
      _spellsLen = input.readUnsignedShort()
      for _i2 in range(0,_spellsLen):
         _item2 = SpellItem(input)
         self.spells.append(_item2)
   
   def _spellPrevisualizationFunc(self,input) :
      self.spellPrevisualization = input.readBoolean()

   def resume(self):
      print("spellPrevisualization :",self.spellPrevisualization)
      for e in self.spells:
         e.resume()
