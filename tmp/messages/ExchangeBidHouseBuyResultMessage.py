class ExchangeBidHouseBuyResultMessage:
   def __init__(self,input):
      self._uidFunc(input)
      self._boughtFunc(input)
   
   def _uidFunc(self,input) :
      self.uid = input.readVarUhInt()
      if(self.uid < 0) :
         raise RuntimeError("Forbidden value (" + self.uid + ") on element of ExchangeBidHouseBuyResultMessage.uid.")
   
   def _boughtFunc(self,input) :
      self.bought = input.readBoolean()