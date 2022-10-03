class PortalInformation:
   def __init__(self,input):
      self._portalIdFunc(input)
      self._areaIdFunc(input)
   
   def _portalIdFunc(self,input) :
      self.portalId = input.readInt()
   
   def _areaIdFunc(self,input) :
      self.areaId = input.readShort()