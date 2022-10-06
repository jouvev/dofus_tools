from src.reseau.types.GuildMember import GuildMember

class GuildInformationsMembersMessage:
   def __init__(self,input):
      self.members = []
      _item1 = None
      _membersLen = input.readUnsignedShort()
      for _i1 in range(0,_membersLen):
         _item1 = GuildMember(input)
         self.members.append(_item1)

   def resume(self):
      for e in self.members:
         e.resume()
