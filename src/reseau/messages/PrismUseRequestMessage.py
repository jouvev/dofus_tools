class PrismUseRequestMessage:
   def __init__(self,input):
      self._moduleToUseFunc(input)
   
   def _moduleToUseFunc(self,input) :
      self.moduleToUse = input.readByte()
      if(self.moduleToUse < 0) :
         raise RuntimeError("Forbidden value (" + str(self.moduleToUse) + ") on element of PrismUseRequestMessage.moduleToUse.")

   def resume(self):
      print("moduleToUse :",self.moduleToUse)
