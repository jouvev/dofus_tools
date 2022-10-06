class StorageKamasUpdateMessage:
   def __init__(self,input):
      self._kamasTotalFunc(input)
   
   def _kamasTotalFunc(self,input) :
      self.kamasTotal = input.readVarUhLong()
      if(self.kamasTotal < 0 or self.kamasTotal > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.kamasTotal) + ") on element of StorageKamasUpdateMessage.kamasTotal.")

   def resume(self):
      print("kamasTotal :",self.kamasTotal)
