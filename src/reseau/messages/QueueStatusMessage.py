class QueueStatusMessage:
   def __init__(self,input):
      self._positionFunc(input)
      self._totalFunc(input)
   
   def _positionFunc(self,input) :
      self.position = input.readUnsignedShort()
      if(self.position < 0 or self.position > 65535) :
         raise RuntimeError("Forbidden value (" + str(self.position) + ") on element of QueueStatusMessage.position.")
   
   def _totalFunc(self,input) :
      self.total = input.readUnsignedShort()
      if(self.total < 0 or self.total > 65535) :
         raise RuntimeError("Forbidden value (" + str(self.total) + ") on element of QueueStatusMessage.total.")

   def resume(self):
      print("position :",self.position)
      print("total :",self.total)
