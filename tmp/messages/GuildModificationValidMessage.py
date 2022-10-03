from tmp.types.GuildEmblem import GuildEmblem
class GuildModificationValidMessage:
   def __init__(self,input):
      self._guildNameFunc(input)
      self.guildEmblem = GuildEmblem(input)
   
   def _guildNameFunc(self,input) :
      self.guildName = input.readUTF()