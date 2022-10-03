from tmp.types.GuildInformations import GuildInformations
class GuildApplicationIsAnsweredMessage:
   def __init__(self,input):
      self._acceptedFunc(input)
      self.guildInformation = GuildInformations(input)
   
   def _acceptedFunc(self,input) :
      self.accepted = input.readBoolean()