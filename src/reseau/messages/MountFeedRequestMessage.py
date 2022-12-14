class MountFeedRequestMessage:
   def __init__(self,input):
      self._mountUidFunc(input)
      self._mountLocationFunc(input)
      self._mountFoodUidFunc(input)
      self._quantityFunc(input)
   
   def _mountUidFunc(self,input) :
      self.mountUid = input.readVarUhInt()
      if(self.mountUid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.mountUid) + ") on element of MountFeedRequestMessage.mountUid.")
   
   def _mountLocationFunc(self,input) :
      self.mountLocation = input.readByte()
   
   def _mountFoodUidFunc(self,input) :
      self.mountFoodUid = input.readVarUhInt()
      if(self.mountFoodUid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.mountFoodUid) + ") on element of MountFeedRequestMessage.mountFoodUid.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of MountFeedRequestMessage.quantity.")

   def resume(self):
      print("mountUid :",self.mountUid)
      print("mountLocation :",self.mountLocation)
      print("mountFoodUid :",self.mountFoodUid)
      print("quantity :",self.quantity)
