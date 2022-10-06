class ObjectSetPositionMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._positionFunc(input)
      self._quantityFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectSetPositionMessage.objectUID.")
   
   def _positionFunc(self,input) :
      self.position = input.readShort()
      if(self.position < 0) :
         raise RuntimeError("Forbidden value (" + str(self.position) + ") on element of ObjectSetPositionMessage.position.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectSetPositionMessage.quantity.")

   def resume(self):
      print("objectUID :",self.objectUID)
      print("position :",self.position)
      print("quantity :",self.quantity)
