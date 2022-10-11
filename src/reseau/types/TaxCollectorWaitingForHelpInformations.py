from src.reseau.types.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from src.reseau.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations

class TaxCollectorWaitingForHelpInformations(TaxCollectorComplementaryInformations):
   def __init__(self,input):
      super().__init__(input)
      self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo(input)

   def resume(self):
      super().resume()
      self.waitingForHelpInfo.resume()
