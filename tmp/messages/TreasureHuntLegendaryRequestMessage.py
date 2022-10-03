class TreasureHuntLegendaryRequestMessage:
   def __init__(self,input):
      self._legendaryIdFunc(input)
   
   def _legendaryIdFunc(self,input) :
      self.legendaryId = input.readVarUhShort()
      if(self.legendaryId < 0) :
         raise RuntimeError("Forbidden value (" + self.legendaryId + ") on element of TreasureHuntLegendaryRequestMessage.legendaryId.")