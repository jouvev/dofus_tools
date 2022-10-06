from tmp.types.FightLoot import FightLoot

class FightResultListEntry:
   def __init__(self,input):
      self._outcomeFunc(input)
      self._waveFunc(input)
      self.rewards = FightLoot(input)
   
   def _outcomeFunc(self,input) :
      self.outcome = input.readVarUhShort()
      if(self.outcome < 0) :
         raise RuntimeError("Forbidden value (" + str(self.outcome) + ") on element of FightResultListEntry.outcome.")
   
   def _waveFunc(self,input) :
      self.wave = input.readByte()
      if(self.wave < 0) :
         raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element of FightResultListEntry.wave.")

   def resume(self):
      print("outcome :",self.outcome)
      print("wave :",self.wave)
      self.rewards.resum()
