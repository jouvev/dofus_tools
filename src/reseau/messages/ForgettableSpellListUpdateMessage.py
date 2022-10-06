from src.reseau.types.ForgettableSpellItem import ForgettableSpellItem

class ForgettableSpellListUpdateMessage:
   def __init__(self,input):
      self.spells = []
      _item2 = None
      self._actionFunc(input)
      _spellsLen = input.readUnsignedShort()
      for _i2 in range(0,_spellsLen):
         _item2 = ForgettableSpellItem(input)
         self.spells.append(_item2)
   
   def _actionFunc(self,input) :
      self.action = input.readByte()
      if(self.action < 0) :
         raise RuntimeError("Forbidden value (" + str(self.action) + ") on element of ForgettableSpellListUpdateMessage.action.")

   def resume(self):
      print("action :",self.action)
      for e in self.spells:
         e.resume()
