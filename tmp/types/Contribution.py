class Contribution:
   def __init__(self,input):
      self._contributorIdFunc(input)
      self._contributorNameFunc(input)
      self._amountFunc(input)
   
   def _contributorIdFunc(self,input) :
      self.contributorId = input.readVarUhLong()
      if(self.contributorId < 0 or self.contributorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.contributorId) + ") on element of Contribution.contributorId.")
   
   def _contributorNameFunc(self,input) :
      self.contributorName = input.readUTF()
   
   def _amountFunc(self,input) :
      self.amount = input.readVarUhLong()
      if(self.amount < 0 or self.amount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.amount) + ") on element of Contribution.amount.")

   def resume(self):
      print("contributorId :",self.contributorId)
      print("contributorName :",self.contributorName)
      print("amount :",self.amount)
