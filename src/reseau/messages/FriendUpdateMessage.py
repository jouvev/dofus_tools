import src.reseau.TypesFactory as pf

class FriendUpdateMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.friendUpdated = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      self.friendUpdated.resume()
