from tmp.types.AllianceInformations import AllianceInformations
from tmp.types.TaxCollectorStaticInformations import TaxCollectorStaticInformations
class TaxCollectorStaticExtendedInformations(TaxCollectorStaticInformations):
   def __init__(self,input):
      super().__init__(input)
      self.allianceIdentity = AllianceInformations(input)