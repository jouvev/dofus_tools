class ForgettableSpellClientActionMessage:
   def __init__(self,input):
      self._spellIdFunc(input)
      self._actionFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readInt()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + self.spellId + ") on element of ForgettableSpellClientActionMessage.spellId.")
   
   def _actionFunc(self,input) :
      self.action = input.readByte()
      if(self.action < 0) :
         raise RuntimeError("Forbidden value (" + self.action + ") on element of ForgettableSpellClientActionMessage.action.")