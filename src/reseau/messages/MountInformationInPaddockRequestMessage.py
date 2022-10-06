class MountInformationInPaddockRequestMessage:
   def __init__(self,input):
      self._mapRideIdFunc(input)
   
   def _mapRideIdFunc(self,input) :
      self.mapRideId = input.readVarInt()

   def resume(self):
      print("mapRideId :",self.mapRideId)
