class ExchangeReplyTaxVendorMessage:
   def __init__(self,input):
      self._objectValueFunc(input)
      self._totalTaxValueFunc(input)
   
   def _objectValueFunc(self,input) :
      self.objectValue = input.readVarUhLong()
      if(self.objectValue < 0 or self.objectValue > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.objectValue + ") on element of ExchangeReplyTaxVendorMessage.objectValue.")
   
   def _totalTaxValueFunc(self,input) :
      self.totalTaxValue = input.readVarUhLong()
      if(self.totalTaxValue < 0 or self.totalTaxValue > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.totalTaxValue + ") on element of ExchangeReplyTaxVendorMessage.totalTaxValue.")