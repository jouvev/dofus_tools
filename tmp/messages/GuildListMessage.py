from tmp.types.GuildInformations import GuildInformations

class GuildListMessage:
   def __init__(self,input):
      self.guilds = []
      _item1 = None
      _guildsLen = input.readUnsignedShort()
      for _i1 in range(0,_guildsLen):
         _item1 = GuildInformations(input)
         self.guilds.append(_item1)

   def resume(self):
      for e in self.guilds:
         e.resume()
