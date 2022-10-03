from tmp.types.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from tmp.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
class TaxCollectorWaitingForHelpInformations(TaxCollectorComplementaryInformations):
   def __init__(self,input):
      super().__init__(input)
      self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo(input)