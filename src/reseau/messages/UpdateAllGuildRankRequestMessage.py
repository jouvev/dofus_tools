from src.reseau.types.GuildRankInformation import GuildRankInformation

class UpdateAllGuildRankRequestMessage:
   def __init__(self,input):
      self.ranks = []
      _item1 = None
      _ranksLen = input.readUnsignedShort()
      for _i1 in range(0,_ranksLen):
         _item1 = GuildRankInformation(input)
         self.ranks.append(_item1)

   def resume(self):
      for e in self.ranks:
         e.resume()
