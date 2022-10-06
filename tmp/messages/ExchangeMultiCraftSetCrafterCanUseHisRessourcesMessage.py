class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage:
   def __init__(self,input):
      self._allowFunc(input)
   
   def _allowFunc(self,input) :
      self.allow = input.readBoolean()

   def resume(self):
      print("allow :",self.allow)
