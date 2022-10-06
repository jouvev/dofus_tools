class AlignmentWarEffortDonatePreviewMessage:
   def __init__(self,input):
      self._xpFunc(input)
   
   def _xpFunc(self,input) :
      self.xp = input.readDouble()
      if(self.xp < -9007199254740992 or self.xp > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.xp) + ") on element of AlignmentWarEffortDonatePreviewMessage.xp.")

   def resume(self):
      print("xp :",self.xp)
