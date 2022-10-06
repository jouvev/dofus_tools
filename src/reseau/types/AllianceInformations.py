from src.reseau.types.GuildEmblem import GuildEmblem
from src.reseau.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations

class AllianceInformations(BasicNamedAllianceInformations):
   def __init__(self,input):
      super().__init__(input)
      self.allianceEmblem = GuildEmblem(input)

   def resume(self):
      super().resume()
      self.allianceEmblem.resum()
