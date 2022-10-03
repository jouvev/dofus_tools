class StorageObjectsRemoveMessage:
   def __init__(self,input):
      self.objectUIDList = []
      _val1 = 0
      _objectUIDListLen = input.readUnsignedShort()
      for _i1 in range(0,_objectUIDListLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of objectUIDList.")
         self.objectUIDList.append(_val1)