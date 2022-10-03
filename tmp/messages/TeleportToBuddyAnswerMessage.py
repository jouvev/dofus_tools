class TeleportToBuddyAnswerMessage:
   def __init__(self,input):
      self._dungeonIdFunc(input)
      self._buddyIdFunc(input)
      self._acceptFunc(input)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + self.dungeonId + ") on element of TeleportToBuddyAnswerMessage.dungeonId.")
   
   def _buddyIdFunc(self,input) :
      self.buddyId = input.readVarUhLong()
      if(self.buddyId < 0 or self.buddyId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.buddyId + ") on element of TeleportToBuddyAnswerMessage.buddyId.")
   
   def _acceptFunc(self,input) :
      self.accept = input.readBoolean()