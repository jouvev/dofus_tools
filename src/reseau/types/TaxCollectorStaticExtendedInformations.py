from src.reseau.types.AllianceInformations import AllianceInformations
from src.reseau.types.TaxCollectorStaticInformations import TaxCollectorStaticInformations

class TaxCollectorStaticExtendedInformations(TaxCollectorStaticInformations):
   def __init__(self,input):
      super().__init__(input)
      self.allianceIdentity = AllianceInformations(input)

   def resume(self):
      super().resume()
      self.allianceIdentity.resume()
