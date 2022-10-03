class AlignmentWarEffortDonationResultMessage:
   def __init__(self,input):
      self._resultFunc(input)
   
   def _resultFunc(self,input) :
      self.result = input.readByte()