class PortalUseRequestMessage:
   def __init__(self,input):
      self._portalIdFunc(input)
   
   def _portalIdFunc(self,input) :
      self.portalId = input.readVarUhInt()
      if(self.portalId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.portalId) + ") on element of PortalUseRequestMessage.portalId.")

   def resume(self):
      print("portalId :",self.portalId)
