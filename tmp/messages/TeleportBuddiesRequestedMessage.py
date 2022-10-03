class TeleportBuddiesRequestedMessage:
   def __init__(self,input):
      self.invalidBuddiesIds = []
      _val3 = None
      self._dungeonIdFunc(input)
      self._inviterIdFunc(input)
      _invalidBuddiesIdsLen = input.readUnsignedShort()
      for _i3 in range(0,_invalidBuddiesIdsLen):
         _val3 = input.readVarUhLong()
         if(_val3 < 0 or _val3 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of invalidBuddiesIds.")
         self.invalidBuddiesIds.append(_val3)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + self.dungeonId + ") on element of TeleportBuddiesRequestedMessage.dungeonId.")
   
   def _inviterIdFunc(self,input) :
      self.inviterId = input.readVarUhLong()
      if(self.inviterId < 0 or self.inviterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.inviterId + ") on element of TeleportBuddiesRequestedMessage.inviterId.")