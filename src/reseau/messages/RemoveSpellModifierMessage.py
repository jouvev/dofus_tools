class RemoveSpellModifierMessage:
   def __init__(self,input):
      self._actorIdFunc(input)
      self._modificationTypeFunc(input)
      self._spellIdFunc(input)
   
   def _actorIdFunc(self,input) :
      self.actorId = input.readDouble()
      if(self.actorId < -9007199254740992 or self.actorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.actorId) + ") on element of RemoveSpellModifierMessage.actorId.")
   
   def _modificationTypeFunc(self,input) :
      self.modificationType = input.readByte()
      if(self.modificationType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.modificationType) + ") on element of RemoveSpellModifierMessage.modificationType.")
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of RemoveSpellModifierMessage.spellId.")

   def resume(self):
      print("actorId :",self.actorId)
      print("modificationType :",self.modificationType)
      print("spellId :",self.spellId)
