from tmp.types.BasicGuildInformations import BasicGuildInformations
from tmp.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations

class TaxCollectorGuildInformations(TaxCollectorComplementaryInformations):
   def __init__(self,input):
      super().__init__(input)
      self.guild = BasicGuildInformations(input)

   def resume(self):
      super().resume()
      self.guild.resum()
