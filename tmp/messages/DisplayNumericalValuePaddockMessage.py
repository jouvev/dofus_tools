class DisplayNumericalValuePaddockMessage:
   def __init__(self,input):
      self._rideIdFunc(input)
      self._valueFunc(input)
      self._typeFunc(input)
   
   def _rideIdFunc(self,input) :
      self.rideId = input.readInt()
   
   def _valueFunc(self,input) :
      self.value = input.readInt()
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + self.type + ") on element of DisplayNumericalValuePaddockMessage.type.")