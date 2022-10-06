class JobAllowMultiCraftRequestMessage:
   def __init__(self,input):
      self._enabledFunc(input)
   
   def _enabledFunc(self,input) :
      self.enabled = input.readBoolean()

   def resume(self):
      print("enabled :",self.enabled)
