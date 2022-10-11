from src.reseau.types.AccountTagInformation import AccountTagInformation

class AcquaintanceSearchMessage:
   def __init__(self,input):
      self.tag = AccountTagInformation(input)

   def resume(self):
      self.tag.resume()
