from src.reseau.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations

class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
   def __init__(self,input):
      super().__init__(input)
      self._kamasFunc(input)
      self._experienceFunc(input)
      self._podsFunc(input)
      self._itemsValueFunc(input)
   
   def _kamasFunc(self,input) :
      self.kamas = input.readVarUhLong()
      if(self.kamas < 0 or self.kamas > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of TaxCollectorLootInformations.kamas.")
   
   def _experienceFunc(self,input) :
      self.experience = input.readVarUhLong()
      if(self.experience < 0 or self.experience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of TaxCollectorLootInformations.experience.")
   
   def _podsFunc(self,input) :
      self.pods = input.readVarUhInt()
      if(self.pods < 0) :
         raise RuntimeError("Forbidden value (" + str(self.pods) + ") on element of TaxCollectorLootInformations.pods.")
   
   def _itemsValueFunc(self,input) :
      self.itemsValue = input.readVarUhLong()
      if(self.itemsValue < 0 or self.itemsValue > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.itemsValue) + ") on element of TaxCollectorLootInformations.itemsValue.")

   def resume(self):
      super().resume()
      print("kamas :",self.kamas)
      print("experience :",self.experience)
      print("pods :",self.pods)
      print("itemsValue :",self.itemsValue)
