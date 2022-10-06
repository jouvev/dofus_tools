from tmp.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from tmp.types.GuildInformations import GuildInformations

class AlliancedGuildFactSheetInformations(GuildInformations):
   def __init__(self,input):
      super().__init__(input)
      self.allianceInfos = BasicNamedAllianceInformations(input)

   def resume(self):
      super().resume()
      self.allianceInfos.resum()
