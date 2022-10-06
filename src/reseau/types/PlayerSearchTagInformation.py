from src.reseau.types.AccountTagInformation import AccountTagInformation
from src.reseau.types.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation

class PlayerSearchTagInformation(AbstractPlayerSearchInformation):
   def __init__(self,input):
      super().__init__(input)
      self.tag = AccountTagInformation(input)

   def resume(self):
      super().resume()
      self.tag.resum()
