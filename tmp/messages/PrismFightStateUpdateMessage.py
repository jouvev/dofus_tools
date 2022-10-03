class PrismFightStateUpdateMessage:
   def __init__(self,input):
      self._stateFunc(input)
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + self.state + ") on element of PrismFightStateUpdateMessage.state.")