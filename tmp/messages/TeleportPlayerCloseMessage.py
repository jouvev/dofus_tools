class TeleportPlayerCloseMessage:
   def __init__(self,input):
      self._mapIdFunc(input)
      self._requesterIdFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of TeleportPlayerCloseMessage.mapId.")
   
   def _requesterIdFunc(self,input) :
      self.requesterId = input.readVarUhLong()
      if(self.requesterId < 0 or self.requesterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.requesterId + ") on element of TeleportPlayerCloseMessage.requesterId.")