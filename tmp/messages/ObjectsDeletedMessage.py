class ObjectsDeletedMessage:
   def __init__(self,input):
      self.objectUID = []
      _val1 = 0
      _objectUIDLen = input.readUnsignedShort()
      for _i1 in range(0,_objectUIDLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of objectUID.")
         self.objectUID.append(_val1)