import tmp.TypesFactory as pf
class GuildInvitationSearchMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.target = pf.TypesFactory.get_instance_id(_id1,input)