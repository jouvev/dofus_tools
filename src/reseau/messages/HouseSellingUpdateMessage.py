from src.reseau.types.AccountTagInformation import AccountTagInformation

class HouseSellingUpdateMessage:
   def __init__(self,input):
      self._houseIdFunc(input)
      self._instanceIdFunc(input)
      self._secondHandFunc(input)
      self._realPriceFunc(input)
      self.buyerTag = AccountTagInformation(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element of HouseSellingUpdateMessage.houseId.")
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseSellingUpdateMessage.instanceId.")
   
   def _secondHandFunc(self,input) :
      self.secondHand = input.readBoolean()
   
   def _realPriceFunc(self,input) :
      self.realPrice = input.readVarUhLong()
      if(self.realPrice < 0 or self.realPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.realPrice) + ") on element of HouseSellingUpdateMessage.realPrice.")

   def resume(self):
      print("houseId :",self.houseId)
      print("instanceId :",self.instanceId)
      print("secondHand :",self.secondHand)
      print("realPrice :",self.realPrice)
      self.buyerTag.resume()
