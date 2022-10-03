from tmp.types.GuildInformations import GuildInformations
from tmp.types.HumanOption import HumanOption
class HumanOptionGuild(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self.guildInformations = GuildInformations(input)