from src.reseau.types.AllianceInformations import AllianceInformations
from src.reseau.types.PrismInformation import PrismInformation

class AlliancePrismInformation(PrismInformation):
   def __init__(self,input):
      super().__init__(input)
      self.alliance = AllianceInformations(input)

   def resume(self):
      super().resume()
      self.alliance.resume()
