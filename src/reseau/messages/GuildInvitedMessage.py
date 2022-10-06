from src.reseau.types.BasicGuildInformations import BasicGuildInformations

class GuildInvitedMessage:
   def __init__(self,input):
      self._recruterIdFunc(input)
      self._recruterNameFunc(input)
      self.guildInfo = BasicGuildInformations(input)
   
   def _recruterIdFunc(self,input) :
      self.recruterId = input.readVarUhLong()
      if(self.recruterId < 0 or self.recruterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.recruterId) + ") on element of GuildInvitedMessage.recruterId.")
   
   def _recruterNameFunc(self,input) :
      self.recruterName = input.readUTF()

   def resume(self):
      print("recruterId :",self.recruterId)
      print("recruterName :",self.recruterName)
      self.guildInfo.resum()
