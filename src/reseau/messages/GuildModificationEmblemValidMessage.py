from src.reseau.types.GuildEmblem import GuildEmblem

class GuildModificationEmblemValidMessage:
   def __init__(self,input):
      self.guildEmblem = GuildEmblem(input)

   def resume(self):
      self.guildEmblem.resume()
