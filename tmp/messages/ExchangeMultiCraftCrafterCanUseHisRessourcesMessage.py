class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage:
   def __init__(self,input):
      self._allowedFunc(input)
   
   def _allowedFunc(self,input) :
      self.allowed = input.readBoolean()

   def resume(self):
      print("allowed :",self.allowed)
