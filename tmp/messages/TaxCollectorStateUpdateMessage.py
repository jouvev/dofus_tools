class TaxCollectorStateUpdateMessage:
   def __init__(self,input):
      self._uniqueIdFunc(input)
      self._stateFunc(input)
   
   def _uniqueIdFunc(self,input) :
      self.uniqueId = input.readDouble()
      if(self.uniqueId < 0 or self.uniqueId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.uniqueId + ") on element of TaxCollectorStateUpdateMessage.uniqueId.")
   
   def _stateFunc(self,input) :
      self.state = input.readByte()