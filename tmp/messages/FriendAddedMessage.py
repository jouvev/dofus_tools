import tmp.TypesFactory as pf
class FriendAddedMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.friendAdded = pf.TypesFactory.get_instance_id(_id1,input)