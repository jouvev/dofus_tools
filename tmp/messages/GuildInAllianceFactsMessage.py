from tmp.messages.GuildFactsMessage import GuildFactsMessage
from tmp.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations
class GuildInAllianceFactsMessage(GuildFactsMessage):
   def __init__(self,input):
      super().__init__(input)
      self.allianceInfos = BasicNamedAllianceInformations(input)