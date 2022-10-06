from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.PaddockBuyableInformations import PaddockBuyableInformations

class PaddockGuildedInformations(PaddockBuyableInformations):
   def __init__(self,input):
      super().__init__(input)
      self._desertedFunc(input)
      self.guildInfo = GuildInformations(input)
   
   def _desertedFunc(self,input) :
      self.deserted = input.readBoolean()

   def resume(self):
      super().resume()
      print("deserted :",self.deserted)
      self.guildInfo.resum()
