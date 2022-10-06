import tmp.TypesFactory as pf
from tmp.types.AllianceFactSheetInformations import AllianceFactSheetInformations
from tmp.types.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations

class AllianceInsiderInfoMessage:
   def __init__(self,input):
      self.guilds = []
      self.prisms = []
      _item2 = None
      _id3 = 0
      _item3 = None
      self.allianceInfos = AllianceFactSheetInformations(input)
      _guildsLen = input.readUnsignedShort()
      for _i2 in range(0,_guildsLen):
         _item2 = GuildInsiderFactSheetInformations(input)
         self.guilds.append(_item2)
      _prismsLen = input.readUnsignedShort()
      for _i3 in range(0,_prismsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.prisms.append(_item3)

   def resume(self):
      self.allianceInfos.resum()
      for e in self.guilds:
         e.resume()
      for e in self.prisms:
         e.resume()
