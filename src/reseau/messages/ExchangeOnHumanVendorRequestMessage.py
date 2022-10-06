class ExchangeOnHumanVendorRequestMessage:
   def __init__(self,input):
      self._humanVendorIdFunc(input)
      self._humanVendorCellFunc(input)
   
   def _humanVendorIdFunc(self,input) :
      self.humanVendorId = input.readVarUhLong()
      if(self.humanVendorId < 0 or self.humanVendorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.humanVendorId) + ") on element of ExchangeOnHumanVendorRequestMessage.humanVendorId.")
   
   def _humanVendorCellFunc(self,input) :
      self.humanVendorCell = input.readVarUhShort()
      if(self.humanVendorCell < 0 or self.humanVendorCell > 559) :
         raise RuntimeError("Forbidden value (" + str(self.humanVendorCell) + ") on element of ExchangeOnHumanVendorRequestMessage.humanVendorCell.")

   def resume(self):
      print("humanVendorId :",self.humanVendorId)
      print("humanVendorCell :",self.humanVendorCell)
