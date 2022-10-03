class ExchangeCraftResultMessage:
   def __init__(self,input):
      self._craftResultFunc(input)
   
   def _craftResultFunc(self,input) :
      self.craftResult = input.readByte()
      if(self.craftResult < 0) :
         raise RuntimeError("Forbidden value (" + self.craftResult + ") on element of ExchangeCraftResultMessage.craftResult.")