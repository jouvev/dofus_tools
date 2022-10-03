class ObjectMovementMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._positionFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectUID + ") on element of ObjectMovementMessage.objectUID.")
   
   def _positionFunc(self,input) :
      self.position = input.readShort()
      if(self.position < 0) :
         raise RuntimeError("Forbidden value (" + self.position + ") on element of ObjectMovementMessage.position.")