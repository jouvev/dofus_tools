class CharacterAlignmentWarEffortProgressionMessage:
   def __init__(self,input):
      self._alignmentWarEffortDailyLimitFunc(input)
      self._alignmentWarEffortDailyDonationFunc(input)
      self._alignmentWarEffortPersonalDonationFunc(input)
   
   def _alignmentWarEffortDailyLimitFunc(self,input) :
      self.alignmentWarEffortDailyLimit = input.readVarUhLong()
      if(self.alignmentWarEffortDailyLimit < 0 or self.alignmentWarEffortDailyLimit > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.alignmentWarEffortDailyLimit) + ") on element of CharacterAlignmentWarEffortProgressionMessage.alignmentWarEffortDailyLimit.")
   
   def _alignmentWarEffortDailyDonationFunc(self,input) :
      self.alignmentWarEffortDailyDonation = input.readVarUhLong()
      if(self.alignmentWarEffortDailyDonation < 0 or self.alignmentWarEffortDailyDonation > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.alignmentWarEffortDailyDonation) + ") on element of CharacterAlignmentWarEffortProgressionMessage.alignmentWarEffortDailyDonation.")
   
   def _alignmentWarEffortPersonalDonationFunc(self,input) :
      self.alignmentWarEffortPersonalDonation = input.readVarUhLong()
      if(self.alignmentWarEffortPersonalDonation < 0 or self.alignmentWarEffortPersonalDonation > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.alignmentWarEffortPersonalDonation) + ") on element of CharacterAlignmentWarEffortProgressionMessage.alignmentWarEffortPersonalDonation.")

   def resume(self):
      print("alignmentWarEffortDailyLimit :",self.alignmentWarEffortDailyLimit)
      print("alignmentWarEffortDailyDonation :",self.alignmentWarEffortDailyDonation)
      print("alignmentWarEffortPersonalDonation :",self.alignmentWarEffortPersonalDonation)
