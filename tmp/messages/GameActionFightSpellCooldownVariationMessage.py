from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage
class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._spellIdFunc(input)
      self._valueFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetId + ") on element of GameActionFightSpellCooldownVariationMessage.targetId.")
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + self.spellId + ") on element of GameActionFightSpellCooldownVariationMessage.spellId.")
   
   def _valueFunc(self,input) :
      self.value = input.readVarShort()