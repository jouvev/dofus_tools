from src.reseau.types.Contribution import Contribution

class GuildChestTabContributionsMessage:
   def __init__(self,input):
      self.contributions = []
      _item1 = None
      _contributionsLen = input.readUnsignedShort()
      for _i1 in range(0,_contributionsLen):
         _item1 = Contribution(input)
         self.contributions.append(_item1)

   def resume(self):
      for e in self.contributions:
         e.resume()
