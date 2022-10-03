class GuildJoinAutomaticallyRequestMessage:
   def __init__(self,input):
      self._guildIdFunc(input)
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readInt()