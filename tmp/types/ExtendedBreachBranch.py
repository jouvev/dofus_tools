from tmp.types.BreachReward import BreachReward
from tmp.types.BreachBranch import BreachBranch
class ExtendedBreachBranch(BreachBranch):
   def __init__(self,input):
      self.rewards = []
      _item1 = None
      super().__init__(input)
      _rewardsLen = input.readUnsignedShort()
      for _i1 in range(0,_rewardsLen):
         _item1 = BreachReward(input)
         self.rewards.append(_item1)
      self._modifierFunc(input)
      self._prizeFunc(input)
   
   def _modifierFunc(self,input) :
      self.modifier = input.readVarInt()
   
   def _prizeFunc(self,input) :
      self.prize = input.readVarUhInt()
      if(self.prize < 0) :
         raise RuntimeError("Forbidden value (" + self.prize + ") on element of ExtendedBreachBranch.prize.")