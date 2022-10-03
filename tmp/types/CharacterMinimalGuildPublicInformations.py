from tmp.types.GuildRankPublicInformation import GuildRankPublicInformation
from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations
class CharacterMinimalGuildPublicInformations(CharacterMinimalInformations):
   def __init__(self,input):
      super().__init__(input)
      self.rank = GuildRankPublicInformation(input)