from tmp.types.HouseInformationsForGuild import HouseInformationsForGuild
class GuildHouseUpdateInformationMessage:
   def __init__(self,input):
      self.housesInformations = HouseInformationsForGuild(input)