class KickHavenBagRequestMessage:
   def __init__(self,input):
      self._guestIdFunc(input)
   
   def _guestIdFunc(self,input) :
      self.guestId = input.readVarUhLong()
      if(self.guestId < 0 or self.guestId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.guestId + ") on element of KickHavenBagRequestMessage.guestId.")