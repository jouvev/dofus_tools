class MountXpRatioMessage:
   def __init__(self,input):
      self._ratioFunc(input)
   
   def _ratioFunc(self,input) :
      self.ratio = input.readByte()
      if(self.ratio < 0) :
         raise RuntimeError("Forbidden value (" + str(self.ratio) + ") on element of MountXpRatioMessage.ratio.")

   def resume(self):
      print("ratio :",self.ratio)
