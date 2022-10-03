from tmp.types.DebtInformation import DebtInformation
class KamaDebtInformation(DebtInformation):
   def __init__(self,input):
      super().__init__(input)
      self._kamasFunc(input)
   
   def _kamasFunc(self,input) :
      self.kamas = input.readVarUhLong()
      if(self.kamas < 0 or self.kamas > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.kamas + ") on element of KamaDebtInformation.kamas.")