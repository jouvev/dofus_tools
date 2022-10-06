from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightSpellImmunityMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._spellIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightSpellImmunityMessage.targetId.")
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of GameActionFightSpellImmunityMessage.spellId.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("spellId :",self.spellId)
