class LivingObjectChangeSkinRequestMessage:
   def __init__(self,input):
      self._livingUIDFunc(input)
      self._livingPositionFunc(input)
      self._skinIdFunc(input)
   
   def _livingUIDFunc(self,input) :
      self.livingUID = input.readVarUhInt()
      if(self.livingUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.livingUID) + ") on element of LivingObjectChangeSkinRequestMessage.livingUID.")
   
   def _livingPositionFunc(self,input) :
      self.livingPosition = input.readUnsignedByte()
      if(self.livingPosition < 0 or self.livingPosition > 255) :
         raise RuntimeError("Forbidden value (" + str(self.livingPosition) + ") on element of LivingObjectChangeSkinRequestMessage.livingPosition.")
   
   def _skinIdFunc(self,input) :
      self.skinId = input.readVarUhInt()
      if(self.skinId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skinId) + ") on element of LivingObjectChangeSkinRequestMessage.skinId.")

   def resume(self):
      print("livingUID :",self.livingUID)
      print("livingPosition :",self.livingPosition)
      print("skinId :",self.skinId)
