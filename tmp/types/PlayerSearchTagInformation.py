from tmp.types.AccountTagInformation import AccountTagInformation
from tmp.types.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation

class PlayerSearchTagInformation(AbstractPlayerSearchInformation):
   def __init__(self,input):
      super().__init__(input)
      self.tag = AccountTagInformation(input)

   def resume(self):
      super().resume()
      self.tag.resum()
