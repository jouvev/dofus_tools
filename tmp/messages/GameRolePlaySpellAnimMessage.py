class GameRolePlaySpellAnimMessage:
   def __init__(self,input):
      self._casterIdFunc(input)
      self._targetCellIdFunc(input)
      self._spellIdFunc(input)
      self._spellLevelFunc(input)
      self._directionFunc(input)
   
   def _casterIdFunc(self,input) :
      self.casterId = input.readVarUhLong()
      if(self.casterId < 0 or self.casterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.casterId) + ") on element of GameRolePlaySpellAnimMessage.casterId.")
   
   def _targetCellIdFunc(self,input) :
      self.targetCellId = input.readVarUhShort()
      if(self.targetCellId < 0 or self.targetCellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.targetCellId) + ") on element of GameRolePlaySpellAnimMessage.targetCellId.")
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of GameRolePlaySpellAnimMessage.spellId.")
   
   def _spellLevelFunc(self,input) :
      self.spellLevel = input.readShort()
      if(self.spellLevel < 1 or self.spellLevel > 32767) :
         raise RuntimeError("Forbidden value (" + str(self.spellLevel) + ") on element of GameRolePlaySpellAnimMessage.spellLevel.")
   
   def _directionFunc(self,input) :
      self.direction = input.readShort()
      if(self.direction < -1 or self.direction > 8) :
         raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of GameRolePlaySpellAnimMessage.direction.")

   def resume(self):
      print("casterId :",self.casterId)
      print("targetCellId :",self.targetCellId)
      print("spellId :",self.spellId)
      print("spellLevel :",self.spellLevel)
      print("direction :",self.direction)
