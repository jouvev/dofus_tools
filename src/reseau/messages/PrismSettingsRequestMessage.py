class PrismSettingsRequestMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._startDefenseTimeFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismSettingsRequestMessage.subAreaId.")
   
   def _startDefenseTimeFunc(self,input) :
      self.startDefenseTime = input.readByte()
      if(self.startDefenseTime < 0) :
         raise RuntimeError("Forbidden value (" + str(self.startDefenseTime) + ") on element of PrismSettingsRequestMessage.startDefenseTime.")

   def resume(self):
      print("subAreaId :",self.subAreaId)
      print("startDefenseTime :",self.startDefenseTime)
