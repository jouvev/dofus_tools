import tmp.TypesFactory as pf

class FriendsListMessage:
   def __init__(self,input):
      self.friendsList = []
      _id1 = 0
      _item1 = None
      _friendsListLen = input.readUnsignedShort()
      for _i1 in range(0,_friendsListLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.friendsList.append(_item1)

   def resume(self):
      for e in self.friendsList:
         e.resume()
