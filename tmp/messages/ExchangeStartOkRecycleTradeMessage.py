class ExchangeStartOkRecycleTradeMessage:
   def __init__(self,input):
      self._percentToPrismFunc(input)
      self._percentToPlayerFunc(input)
   
   def _percentToPrismFunc(self,input) :
      self.percentToPrism = input.readShort()
      if(self.percentToPrism < 0) :
         raise RuntimeError("Forbidden value (" + str(self.percentToPrism) + ") on element of ExchangeStartOkRecycleTradeMessage.percentToPrism.")
   
   def _percentToPlayerFunc(self,input) :
      self.percentToPlayer = input.readShort()
      if(self.percentToPlayer < 0) :
         raise RuntimeError("Forbidden value (" + str(self.percentToPlayer) + ") on element of ExchangeStartOkRecycleTradeMessage.percentToPlayer.")

   def resume(self):
      print("percentToPrism :",self.percentToPrism)
      print("percentToPlayer :",self.percentToPlayer)
