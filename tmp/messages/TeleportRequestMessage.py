class TeleportRequestMessage:
   def __init__(self,input):
      self._sourceTypeFunc(input)
      self._destinationTypeFunc(input)
      self._mapIdFunc(input)
   
   def _sourceTypeFunc(self,input) :
      self.sourceType = input.readByte()
      if(self.sourceType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.sourceType) + ") on element of TeleportRequestMessage.sourceType.")
   
   def _destinationTypeFunc(self,input) :
      self.destinationType = input.readByte()
      if(self.destinationType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.destinationType) + ") on element of TeleportRequestMessage.destinationType.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of TeleportRequestMessage.mapId.")

   def resume(self):
      print("sourceType :",self.sourceType)
      print("destinationType :",self.destinationType)
      print("mapId :",self.mapId)
