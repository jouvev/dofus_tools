from tmp.types.GuildEmblem import GuildEmblem
from tmp.types.BasicGuildInformations import BasicGuildInformations
class GuildInformations(BasicGuildInformations):
   def __init__(self,input):
      super().__init__(input)
      self.guildEmblem = GuildEmblem(input)