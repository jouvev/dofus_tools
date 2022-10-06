class AlignmentRankUpdateMessage:
   def __init__(self,input):
      self._alignmentRankFunc(input)
      self._verboseFunc(input)
   
   def _alignmentRankFunc(self,input) :
      self.alignmentRank = input.readByte()
      if(self.alignmentRank < 0) :
         raise RuntimeError("Forbidden value (" + str(self.alignmentRank) + ") on element of AlignmentRankUpdateMessage.alignmentRank.")
   
   def _verboseFunc(self,input) :
      self.verbose = input.readBoolean()

   def resume(self):
      print("alignmentRank :",self.alignmentRank)
      print("verbose :",self.verbose)
