from tmp.types.GuildInformations import GuildInformations
from tmp.types.PaddockBuyableInformations import PaddockBuyableInformations
class PaddockGuildedInformations(PaddockBuyableInformations):
   def __init__(self,input):
      super().__init__(input)
      self._desertedFunc(input)
      self.guildInfo = GuildInformations(input)
   
   def _desertedFunc(self,input) :
      self.deserted = input.readBoolean()