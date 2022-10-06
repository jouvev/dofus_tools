class GroupTeleportPlayerOfferMessage:
   def __init__(self,input):
      self._mapIdFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._timeLeftFunc(input)
      self._requesterIdFunc(input)
      self._requesterNameFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of GroupTeleportPlayerOfferMessage.mapId.")
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
   
   def _timeLeftFunc(self,input) :
      self.timeLeft = input.readVarUhInt()
      if(self.timeLeft < 0) :
         raise RuntimeError("Forbidden value (" + str(self.timeLeft) + ") on element of GroupTeleportPlayerOfferMessage.timeLeft.")
   
   def _requesterIdFunc(self,input) :
      self.requesterId = input.readVarUhLong()
      if(self.requesterId < 0 or self.requesterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.requesterId) + ") on element of GroupTeleportPlayerOfferMessage.requesterId.")
   
   def _requesterNameFunc(self,input) :
      self.requesterName = input.readUTF()

   def resume(self):
      print("mapId :",self.mapId)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("timeLeft :",self.timeLeft)
      print("requesterId :",self.requesterId)
      print("requesterName :",self.requesterName)
