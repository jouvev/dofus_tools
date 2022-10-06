class HouseSellRequestMessage:
   def __init__(self,input):
      self._instanceIdFunc(input)
      self._amountFunc(input)
      self._forSaleFunc(input)
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseSellRequestMessage.instanceId.")
   
   def _amountFunc(self,input) :
      self.amount = input.readVarUhLong()
      if(self.amount < 0 or self.amount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.amount) + ") on element of HouseSellRequestMessage.amount.")
   
   def _forSaleFunc(self,input) :
      self.forSale = input.readBoolean()

   def resume(self):
      print("instanceId :",self.instanceId)
      print("amount :",self.amount)
      print("forSale :",self.forSale)
