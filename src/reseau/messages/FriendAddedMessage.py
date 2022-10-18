import src.reseau.TypesFactory as pf

class FriendAddedMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.friendAdded = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      self.friendAdded.resume()
