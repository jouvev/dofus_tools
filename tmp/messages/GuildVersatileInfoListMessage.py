import tmp.TypesFactory as pf

class GuildVersatileInfoListMessage:
   def __init__(self,input):
      self.guilds = []
      _id1 = 0
      _item1 = None
      _guildsLen = input.readUnsignedShort()
      for _i1 in range(0,_guildsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.guilds.append(_item1)

   def resume(self):
      for e in self.guilds:
         e.resume()
