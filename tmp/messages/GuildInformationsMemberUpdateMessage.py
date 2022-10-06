from tmp.types.GuildMember import GuildMember

class GuildInformationsMemberUpdateMessage:
   def __init__(self,input):
      self.member = GuildMember(input)

   def resume(self):
      self.member.resum()
