from src.reseau.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._spellIdFunc(input)
      self._valueFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightSpellCooldownVariationMessage.targetId.")
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of GameActionFightSpellCooldownVariationMessage.spellId.")
   
   def _valueFunc(self,input) :
      self.value = input.readVarShort()

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("spellId :",self.spellId)
      print("value :",self.value)
