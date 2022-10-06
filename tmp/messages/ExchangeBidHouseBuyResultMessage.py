class ExchangeBidHouseBuyResultMessage:
   def __init__(self,input):
      self._uidFunc(input)
      self._boughtFunc(input)
   
   def _uidFunc(self,input) :
      self.uid = input.readVarUhInt()
      if(self.uid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of ExchangeBidHouseBuyResultMessage.uid.")
   
   def _boughtFunc(self,input) :
      self.bought = input.readBoolean()

   def resume(self):
      print("uid :",self.uid)
      print("bought :",self.bought)
