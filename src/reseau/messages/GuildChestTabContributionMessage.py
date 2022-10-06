class GuildChestTabContributionMessage:
   def __init__(self,input):
      self._tabNumberFunc(input)
      self._requiredAmountFunc(input)
      self._currentAmountFunc(input)
      self._chestContributionEnrollmentDelayFunc(input)
      self._chestContributionDelayFunc(input)
   
   def _tabNumberFunc(self,input) :
      self.tabNumber = input.readVarUhInt()
      if(self.tabNumber < 0) :
         raise RuntimeError("Forbidden value (" + str(self.tabNumber) + ") on element of GuildChestTabContributionMessage.tabNumber.")
   
   def _requiredAmountFunc(self,input) :
      self.requiredAmount = input.readVarUhLong()
      if(self.requiredAmount < 0 or self.requiredAmount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.requiredAmount) + ") on element of GuildChestTabContributionMessage.requiredAmount.")
   
   def _currentAmountFunc(self,input) :
      self.currentAmount = input.readVarUhLong()
      if(self.currentAmount < 0 or self.currentAmount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.currentAmount) + ") on element of GuildChestTabContributionMessage.currentAmount.")
   
   def _chestContributionEnrollmentDelayFunc(self,input) :
      self.chestContributionEnrollmentDelay = input.readDouble()
      if(self.chestContributionEnrollmentDelay < 0 or self.chestContributionEnrollmentDelay > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.chestContributionEnrollmentDelay) + ") on element of GuildChestTabContributionMessage.chestContributionEnrollmentDelay.")
   
   def _chestContributionDelayFunc(self,input) :
      self.chestContributionDelay = input.readDouble()
      if(self.chestContributionDelay < 0 or self.chestContributionDelay > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.chestContributionDelay) + ") on element of GuildChestTabContributionMessage.chestContributionDelay.")

   def resume(self):
      print("tabNumber :",self.tabNumber)
      print("requiredAmount :",self.requiredAmount)
      print("currentAmount :",self.currentAmount)
      print("chestContributionEnrollmentDelay :",self.chestContributionEnrollmentDelay)
      print("chestContributionDelay :",self.chestContributionDelay)
