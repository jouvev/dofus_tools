from src.reseau.types.GuildRankPublicInformation import GuildRankPublicInformation
from src.reseau.types.CharacterMinimalInformations import CharacterMinimalInformations

class CharacterMinimalGuildPublicInformations(CharacterMinimalInformations):
   def __init__(self,input):
      super().__init__(input)
      self.rank = GuildRankPublicInformation(input)

   def resume(self):
      super().resume()
      self.rank.resume()
