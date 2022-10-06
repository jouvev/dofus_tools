from src.reseau.types.GuildEmblem import GuildEmblem
from src.reseau.types.BasicGuildInformations import BasicGuildInformations

class GuildInformations(BasicGuildInformations):
   def __init__(self,input):
      super().__init__(input)
      self.guildEmblem = GuildEmblem(input)

   def resume(self):
      super().resume()
      self.guildEmblem.resum()
