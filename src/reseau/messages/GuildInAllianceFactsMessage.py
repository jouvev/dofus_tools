from src.reseau.messages.GuildFactsMessage import GuildFactsMessage
from src.reseau.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations

class GuildInAllianceFactsMessage(GuildFactsMessage):
   def __init__(self,input):
      super().__init__(input)
      self.allianceInfos = BasicNamedAllianceInformations(input)

   def resume(self):
      super().resume()
      self.allianceInfos.resume()
