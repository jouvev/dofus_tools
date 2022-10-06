class ProtectedEntityWaitingForHelpInfo:
   def __init__(self,input):
      self._timeLeftBeforeFightFunc(input)
      self._waitTimeForPlacementFunc(input)
      self._nbPositionForDefensorsFunc(input)
   
   def _timeLeftBeforeFightFunc(self,input) :
      self.timeLeftBeforeFight = input.readInt()
   
   def _waitTimeForPlacementFunc(self,input) :
      self.waitTimeForPlacement = input.readInt()
   
   def _nbPositionForDefensorsFunc(self,input) :
      self.nbPositionForDefensors = input.readByte()
      if(self.nbPositionForDefensors < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbPositionForDefensors) + ") on element of ProtectedEntityWaitingForHelpInfo.nbPositionForDefensors.")

   def resume(self):
      print("timeLeftBeforeFight :",self.timeLeftBeforeFight)
      print("waitTimeForPlacement :",self.waitTimeForPlacement)
      print("nbPositionForDefensors :",self.nbPositionForDefensors)
