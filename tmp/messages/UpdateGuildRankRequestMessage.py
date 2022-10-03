from tmp.types.GuildRankInformation import GuildRankInformation
class UpdateGuildRankRequestMessage:
   def __init__(self,input):
      self.rank = GuildRankInformation(input)