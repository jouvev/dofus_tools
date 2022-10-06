from src.reseau.types.CharacterMinimalInformations import CharacterMinimalInformations
from src.reseau.types.ObjectEffectInteger import ObjectEffectInteger

class BreachStateMessage:
   def __init__(self,input):
      self.bonuses = []
      _item2 = None
      self.owner = CharacterMinimalInformations(input)
      _bonusesLen = input.readUnsignedShort()
      for _i2 in range(0,_bonusesLen):
         _item2 = ObjectEffectInteger(input)
         self.bonuses.append(_item2)
      self._bugdetFunc(input)
      self._savedFunc(input)
   
   def _bugdetFunc(self,input) :
      self.bugdet = input.readVarUhInt()
      if(self.bugdet < 0) :
         raise RuntimeError("Forbidden value (" + str(self.bugdet) + ") on element of BreachStateMessage.bugdet.")
   
   def _savedFunc(self,input) :
      self.saved = input.readBoolean()

   def resume(self):
      print("bugdet :",self.bugdet)
      print("saved :",self.saved)
      self.owner.resum()
      for e in self.bonuses:
         e.resume()
