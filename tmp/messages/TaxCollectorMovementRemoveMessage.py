class TaxCollectorMovementRemoveMessage:
   def __init__(self,input):
      self._collectorIdFunc(input)
   
   def _collectorIdFunc(self,input) :
      self.collectorId = input.readDouble()
      if(self.collectorId < 0 or self.collectorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.collectorId) + ") on element of TaxCollectorMovementRemoveMessage.collectorId.")

   def resume(self):
      print("collectorId :",self.collectorId)
