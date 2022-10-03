class GuildSpellUpgradeRequestMessage:
   def __init__(self,input):
      self._spellIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readInt()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + self.spellId + ") on element of GuildSpellUpgradeRequestMessage.spellId.")