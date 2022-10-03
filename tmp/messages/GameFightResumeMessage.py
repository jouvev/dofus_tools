from tmp.messages.GameFightSpectateMessage import GameFightSpectateMessage
from tmp.types.GameFightSpellCooldown import GameFightSpellCooldown
class GameFightResumeMessage(GameFightSpectateMessage):
   def __init__(self,input):
      self.spellCooldowns = []
      _item1 = None
      super().__init__(input)
      _spellCooldownsLen = input.readUnsignedShort()
      for _i1 in range(0,_spellCooldownsLen):
         _item1 = GameFightSpellCooldown(input)
         self.spellCooldowns.append(_item1)
      self._summonCountFunc(input)
      self._bombCountFunc(input)
   
   def _summonCountFunc(self,input) :
      self.summonCount = input.readByte()
      if(self.summonCount < 0) :
         raise RuntimeError("Forbidden value (" + self.summonCount + ") on element of GameFightResumeMessage.summonCount.")
   
   def _bombCountFunc(self,input) :
      self.bombCount = input.readByte()
      if(self.bombCount < 0) :
         raise RuntimeError("Forbidden value (" + self.bombCount + ") on element of GameFightResumeMessage.bombCount.")