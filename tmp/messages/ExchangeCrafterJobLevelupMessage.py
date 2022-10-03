class ExchangeCrafterJobLevelupMessage:
   def __init__(self,input):
      self._crafterJobLevelFunc(input)
   
   def _crafterJobLevelFunc(self,input) :
      self.crafterJobLevel = input.readUnsignedByte()
      if(self.crafterJobLevel < 0 or self.crafterJobLevel > 255) :
         raise RuntimeError("Forbidden value (" + self.crafterJobLevel + ") on element of ExchangeCrafterJobLevelupMessage.crafterJobLevel.")