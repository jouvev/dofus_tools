from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.HumanOption import HumanOption

class HumanOptionGuild(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self.guildInformations = GuildInformations(input)

   def resume(self):
      super().resume()
      self.guildInformations.resum()
