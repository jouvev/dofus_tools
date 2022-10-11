from src.reseau.types.GuildEmblem import GuildEmblem

class AllianceModificationEmblemValidMessage:
   def __init__(self,input):
      self.Alliancemblem = GuildEmblem(input)

   def resume(self):
      self.Alliancemblem.resume()
