class ChangeMapMessage:
   def __init__(self,input):
      self._mapIdFunc(input)
      self._autopilotFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of ChangeMapMessage.mapId.")
   
   def _autopilotFunc(self,input) :
      self.autopilot = input.readBoolean()

   def resume(self):
      print("mapId :",self.mapId)
      print("autopilot :",self.autopilot)
