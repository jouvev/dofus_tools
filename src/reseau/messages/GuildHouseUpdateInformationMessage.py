from src.reseau.types.HouseInformationsForGuild import HouseInformationsForGuild

class GuildHouseUpdateInformationMessage:
   def __init__(self,input):
      self.housesInformations = HouseInformationsForGuild(input)

   def resume(self):
      self.housesInformations.resum()
