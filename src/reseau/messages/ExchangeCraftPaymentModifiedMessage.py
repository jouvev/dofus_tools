class ExchangeCraftPaymentModifiedMessage:
   def __init__(self,input):
      self._goldSumFunc(input)
   
   def _goldSumFunc(self,input) :
      self.goldSum = input.readVarUhLong()
      if(self.goldSum < 0 or self.goldSum > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.goldSum) + ") on element of ExchangeCraftPaymentModifiedMessage.goldSum.")

   def resume(self):
      print("goldSum :",self.goldSum)
