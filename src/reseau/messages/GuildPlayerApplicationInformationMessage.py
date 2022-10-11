from src.reseau.messages.GuildPlayerApplicationAbstractMessage import GuildPlayerApplicationAbstractMessage
from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.GuildApplicationInformation import GuildApplicationInformation

class GuildPlayerApplicationInformationMessage(GuildPlayerApplicationAbstractMessage):
   def __init__(self,input):
      super().__init__(input)
      self.guildInformation = GuildInformations(input)
      self.apply = GuildApplicationInformation(input)

   def resume(self):
      super().resume()
      self.guildInformation.resume()
      self.apply.resume()
