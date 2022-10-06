class TreasureHuntAvailableRetryCountUpdateMessage:
   def __init__(self,input):
      self._questTypeFunc(input)
      self._availableRetryCountFunc(input)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.questType) + ") on element of TreasureHuntAvailableRetryCountUpdateMessage.questType.")
   
   def _availableRetryCountFunc(self,input) :
      self.availableRetryCount = input.readInt()

   def resume(self):
      print("questType :",self.questType)
      print("availableRetryCount :",self.availableRetryCount)
