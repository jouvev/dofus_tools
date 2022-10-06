class AlignmentWarEffortInformation:
   def __init__(self,input):
      self._alignmentSideFunc(input)
      self._alignmentWarEffortFunc(input)
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()
   
   def _alignmentWarEffortFunc(self,input) :
      self.alignmentWarEffort = input.readVarUhLong()
      if(self.alignmentWarEffort < 0 or self.alignmentWarEffort > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.alignmentWarEffort) + ") on element of AlignmentWarEffortInformation.alignmentWarEffort.")

   def resume(self):
      print("alignmentSide :",self.alignmentSide)
      print("alignmentWarEffort :",self.alignmentWarEffort)
