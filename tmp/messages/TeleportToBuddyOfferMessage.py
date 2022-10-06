class TeleportToBuddyOfferMessage:
   def __init__(self,input):
      self._dungeonIdFunc(input)
      self._buddyIdFunc(input)
      self._timeLeftFunc(input)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dungeonId) + ") on element of TeleportToBuddyOfferMessage.dungeonId.")
   
   def _buddyIdFunc(self,input) :
      self.buddyId = input.readVarUhLong()
      if(self.buddyId < 0 or self.buddyId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.buddyId) + ") on element of TeleportToBuddyOfferMessage.buddyId.")
   
   def _timeLeftFunc(self,input) :
      self.timeLeft = input.readVarUhInt()
      if(self.timeLeft < 0) :
         raise RuntimeError("Forbidden value (" + str(self.timeLeft) + ") on element of TeleportToBuddyOfferMessage.timeLeft.")

   def resume(self):
      print("dungeonId :",self.dungeonId)
      print("buddyId :",self.buddyId)
      print("timeLeft :",self.timeLeft)
