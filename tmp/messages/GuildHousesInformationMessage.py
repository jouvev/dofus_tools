from tmp.types.HouseInformationsForGuild import HouseInformationsForGuild

class GuildHousesInformationMessage:
   def __init__(self,input):
      self.housesInformations = []
      _item1 = None
      _housesInformationsLen = input.readUnsignedShort()
      for _i1 in range(0,_housesInformationsLen):
         _item1 = HouseInformationsForGuild(input)
         self.housesInformations.append(_item1)

   def resume(self):
      for e in self.housesInformations:
         e.resume()
