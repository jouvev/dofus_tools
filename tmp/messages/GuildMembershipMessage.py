from tmp.messages.GuildJoinedMessage import GuildJoinedMessage
class GuildMembershipMessage(GuildJoinedMessage):
   def __init__(self,input):
      super().__init__(input)