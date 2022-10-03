class ObjectSetPositionMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._positionFunc(input)
      self._quantityFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectUID + ") on element of ObjectSetPositionMessage.objectUID.")
   
   def _positionFunc(self,input) :
      self.position = input.readShort()
      if(self.position < 0) :
         raise RuntimeError("Forbidden value (" + self.position + ") on element of ObjectSetPositionMessage.position.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ObjectSetPositionMessage.quantity.")