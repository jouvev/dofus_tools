from src.reseau.types.GuildInformations import GuildInformations

class GuildApplicationIsAnsweredMessage:
   def __init__(self,input):
      self._acceptedFunc(input)
      self.guildInformation = GuildInformations(input)
   
   def _acceptedFunc(self,input) :
      self.accepted = input.readBoolean()

   def resume(self):
      print("accepted :",self.accepted)
      self.guildInformation.resume()
