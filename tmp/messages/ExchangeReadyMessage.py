class ExchangeReadyMessage:
   def __init__(self,input):
      self._readyFunc(input)
      self._stepFunc(input)
   
   def _readyFunc(self,input) :
      self.ready = input.readBoolean()
   
   def _stepFunc(self,input) :
      self.step = input.readVarUhShort()
      if(self.step < 0) :
         raise RuntimeError("Forbidden value (" + str(self.step) + ") on element of ExchangeReadyMessage.step.")

   def resume(self):
      print("ready :",self.ready)
      print("step :",self.step)
