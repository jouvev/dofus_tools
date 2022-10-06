class BasicLatencyStatsMessage:
   def __init__(self,input):
      self._latencyFunc(input)
      self._sampleCountFunc(input)
      self._maxFunc(input)
   
   def _latencyFunc(self,input) :
      self.latency = input.readUnsignedShort()
      if(self.latency < 0 or self.latency > 65535) :
         raise RuntimeError("Forbidden value (" + str(self.latency) + ") on element of BasicLatencyStatsMessage.latency.")
   
   def _sampleCountFunc(self,input) :
      self.sampleCount = input.readVarUhShort()
      if(self.sampleCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.sampleCount) + ") on element of BasicLatencyStatsMessage.sampleCount.")
   
   def _maxFunc(self,input) :
      self.max = input.readVarUhShort()
      if(self.max < 0) :
         raise RuntimeError("Forbidden value (" + str(self.max) + ") on element of BasicLatencyStatsMessage.max.")

   def resume(self):
      print("latency :",self.latency)
      print("sampleCount :",self.sampleCount)
      print("max :",self.max)
