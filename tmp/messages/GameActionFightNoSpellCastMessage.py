class GameActionFightNoSpellCastMessage:
   def __init__(self,input):
      self._spellLevelIdFunc(input)
   
   def _spellLevelIdFunc(self,input) :
      self.spellLevelId = input.readVarUhInt()
      if(self.spellLevelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellLevelId) + ") on element of GameActionFightNoSpellCastMessage.spellLevelId.")

   def resume(self):
      print("spellLevelId :",self.spellLevelId)
