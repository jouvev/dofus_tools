class GuildChestTabLastContributionMessage:
   def __init__(self,input):
      self._lastContributionDateFunc(input)
   
   def _lastContributionDateFunc(self,input) :
      self.lastContributionDate = input.readDouble()
      if(self.lastContributionDate < 0 or self.lastContributionDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.lastContributionDate) + ") on element of GuildChestTabLastContributionMessage.lastContributionDate.")

   def resume(self):
      print("lastContributionDate :",self.lastContributionDate)
