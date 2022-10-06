from src.reseau.types.GameFightSpellCooldown import GameFightSpellCooldown

class GameFightResumeSlaveInfo:
   def __init__(self,input):
      self.spellCooldowns = []
      _item2 = None
      self._slaveIdFunc(input)
      _spellCooldownsLen = input.readUnsignedShort()
      for _i2 in range(0,_spellCooldownsLen):
         _item2 = GameFightSpellCooldown(input)
         self.spellCooldowns.append(_item2)
      self._summonCountFunc(input)
      self._bombCountFunc(input)
   
   def _slaveIdFunc(self,input) :
      self.slaveId = input.readDouble()
      if(self.slaveId < -9007199254740992 or self.slaveId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.slaveId) + ") on element of GameFightResumeSlaveInfo.slaveId.")
   
   def _summonCountFunc(self,input) :
      self.summonCount = input.readByte()
      if(self.summonCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.summonCount) + ") on element of GameFightResumeSlaveInfo.summonCount.")
   
   def _bombCountFunc(self,input) :
      self.bombCount = input.readByte()
      if(self.bombCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.bombCount) + ") on element of GameFightResumeSlaveInfo.bombCount.")

   def resume(self):
      print("slaveId :",self.slaveId)
      print("summonCount :",self.summonCount)
      print("bombCount :",self.bombCount)
      for e in self.spellCooldowns:
         e.resume()
