from tmp.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._followedIdFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.success = bool(bin(_box0)[2:].zfill(8)[0])
      self.isFollowed = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _followedIdFunc(self,input) :
      self.followedId = input.readVarUhLong()
      if(self.followedId < 0 or self.followedId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.followedId) + ") on element of PartyFollowStatusUpdateMessage.followedId.")

   def resume(self):
      super().resume()
      print("followedId :",self.followedId)
