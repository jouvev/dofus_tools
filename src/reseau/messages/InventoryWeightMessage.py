class InventoryWeightMessage:
   def __init__(self,input):
      self._inventoryWeightFunc(input)
      self._shopWeightFunc(input)
      self._weightMaxFunc(input)
   
   def _inventoryWeightFunc(self,input) :
      self.inventoryWeight = input.readVarUhInt()
      if(self.inventoryWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.inventoryWeight) + ") on element of InventoryWeightMessage.inventoryWeight.")
   
   def _shopWeightFunc(self,input) :
      self.shopWeight = input.readVarUhInt()
      if(self.shopWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.shopWeight) + ") on element of InventoryWeightMessage.shopWeight.")
   
   def _weightMaxFunc(self,input) :
      self.weightMax = input.readVarUhInt()
      if(self.weightMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.weightMax) + ") on element of InventoryWeightMessage.weightMax.")

   def resume(self):
      print("inventoryWeight :",self.inventoryWeight)
      print("shopWeight :",self.shopWeight)
      print("weightMax :",self.weightMax)
