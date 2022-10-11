from src.reseau.types.AccountTagInformation import AccountTagInformation

class AbstractContactInformations:
   def __init__(self,input):
      self._accountIdFunc(input)
      self.accountTag = AccountTagInformation(input)
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of AbstractContactInformations.accountId.")

   def resume(self):
      print("accountId :",self.accountId)
      self.accountTag.resume()
