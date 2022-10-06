class HouseInformations:
   def __init__(self,input):
      self._houseIdFunc(input)
      self._modelIdFunc(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element of HouseInformations.houseId.")
   
   def _modelIdFunc(self,input) :
      self.modelId = input.readVarUhShort()
      if(self.modelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of HouseInformations.modelId.")

   def resume(self):
      print("houseId :",self.houseId)
      print("modelId :",self.modelId)
