class AlignmentWarEffortDonateRequestMessage:
   def __init__(self,input):
      self._donationFunc(input)
   
   def _donationFunc(self,input) :
      self.donation = input.readVarUhLong()
      if(self.donation < 0 or self.donation > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.donation) + ") on element of AlignmentWarEffortDonateRequestMessage.donation.")

   def resume(self):
      print("donation :",self.donation)
