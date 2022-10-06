from tmp.types.BreachReward import BreachReward

class BreachRewardsMessage:
   def __init__(self,input):
      self.rewards = []
      _item1 = None
      _rewardsLen = input.readUnsignedShort()
      for _i1 in range(0,_rewardsLen):
         _item1 = BreachReward(input)
         self.rewards.append(_item1)

   def resume(self):
      for e in self.rewards:
         e.resume()
