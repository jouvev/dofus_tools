class LivingObjectDissociateMessage:
   def __init__(self,input):
      self._livingUIDFunc(input)
      self._livingPositionFunc(input)
   
   def _livingUIDFunc(self,input) :
      self.livingUID = input.readVarUhInt()
      if(self.livingUID < 0) :
         raise RuntimeError("Forbidden value (" + self.livingUID + ") on element of LivingObjectDissociateMessage.livingUID.")
   
   def _livingPositionFunc(self,input) :
      self.livingPosition = input.readUnsignedByte()
      if(self.livingPosition < 0 or self.livingPosition > 255) :
         raise RuntimeError("Forbidden value (" + self.livingPosition + ") on element of LivingObjectDissociateMessage.livingPosition.")