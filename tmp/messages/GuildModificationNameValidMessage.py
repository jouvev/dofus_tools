class GuildModificationNameValidMessage:
   def __init__(self,input):
      self._guildNameFunc(input)
   
   def _guildNameFunc(self,input) :
      self.guildName = input.readUTF()