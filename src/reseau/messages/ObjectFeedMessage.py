from src.reseau.types.ObjectItemQuantity import ObjectItemQuantity

class ObjectFeedMessage:
   def __init__(self,input):
      self.meal = []
      _item2 = None
      self._objectUIDFunc(input)
      _mealLen = input.readUnsignedShort()
      for _i2 in range(0,_mealLen):
         _item2 = ObjectItemQuantity(input)
         self.meal.append(_item2)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectFeedMessage.objectUID.")

   def resume(self):
      print("objectUID :",self.objectUID)
      for e in self.meal:
         e.resume()
