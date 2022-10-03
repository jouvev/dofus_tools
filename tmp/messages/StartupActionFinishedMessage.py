class StartupActionFinishedMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._actionIdFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.success = bool(bin(_box0)[2:].zfill(8)[0])
      self.automaticAction = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _actionIdFunc(self,input) :
      self.actionId = input.readInt()
      if(self.actionId < 0) :
         raise RuntimeError("Forbidden value (" + self.actionId + ") on element of StartupActionFinishedMessage.actionId.")