from tmp.messages.GuildPlayerApplicationAbstractMessage import GuildPlayerApplicationAbstractMessage
from tmp.types.GuildInformations import GuildInformations
from tmp.types.GuildApplicationInformation import GuildApplicationInformation

class GuildPlayerApplicationInformationMessage(GuildPlayerApplicationAbstractMessage):
   def __init__(self,input):
      super().__init__(input)
      self.guildInformation = GuildInformations(input)
      self.apply = GuildApplicationInformation(input)

   def resume(self):
      super().resume()
      self.guildInformation.resum()
      self.apply.resum()
