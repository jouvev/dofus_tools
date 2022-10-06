from src.reseau.messages.SocialNoticeMessage import SocialNoticeMessage

class BulletinMessage(SocialNoticeMessage):
   def __init__(self,input):
      super().__init__(input)
      self._lastNotifiedTimestampFunc(input)
   
   def _lastNotifiedTimestampFunc(self,input) :
      self.lastNotifiedTimestamp = input.readInt()
      if(self.lastNotifiedTimestamp < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastNotifiedTimestamp) + ") on element of BulletinMessage.lastNotifiedTimestamp.")

   def resume(self):
      super().resume()
      print("lastNotifiedTimestamp :",self.lastNotifiedTimestamp)
