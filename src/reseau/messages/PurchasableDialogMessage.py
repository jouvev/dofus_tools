class PurchasableDialogMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._purchasableIdFunc(input)
      self._purchasableInstanceIdFunc(input)
      self._priceFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.buyOrSell = bool(bin(_box0)[2:].zfill(8)[0])
      self.secondHand = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _purchasableIdFunc(self,input) :
      self.purchasableId = input.readDouble()
      if(self.purchasableId < 0 or self.purchasableId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.purchasableId) + ") on element of PurchasableDialogMessage.purchasableId.")
   
   def _purchasableInstanceIdFunc(self,input) :
      self.purchasableInstanceId = input.readInt()
      if(self.purchasableInstanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.purchasableInstanceId) + ") on element of PurchasableDialogMessage.purchasableInstanceId.")
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of PurchasableDialogMessage.price.")

   def resume(self):
      print("purchasableId :",self.purchasableId)
      print("purchasableInstanceId :",self.purchasableInstanceId)
      print("price :",self.price)
