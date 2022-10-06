class MountSetXpRatioRequestMessage:
   def __init__(self,input):
      self._xpRatioFunc(input)
   
   def _xpRatioFunc(self,input) :
      self.xpRatio = input.readByte()
      if(self.xpRatio < 0) :
         raise RuntimeError("Forbidden value (" + str(self.xpRatio) + ") on element of MountSetXpRatioRequestMessage.xpRatio.")

   def resume(self):
      print("xpRatio :",self.xpRatio)
