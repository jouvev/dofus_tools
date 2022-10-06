from src.reseau.types.GuildEmblem import GuildEmblem

class GuildCreationValidMessage:
   def __init__(self,input):
      self._guildNameFunc(input)
      self.guildEmblem = GuildEmblem(input)
   
   def _guildNameFunc(self,input) :
      self.guildName = input.readUTF()

   def resume(self):
      print("guildName :",self.guildName)
      self.guildEmblem.resum()
