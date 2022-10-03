class ExchangeShopStockMultiMovementRemovedMessage:
   def __init__(self,input):
      self.objectIdList = []
      _val1 = 0
      _objectIdListLen = input.readUnsignedShort()
      for _i1 in range(0,_objectIdListLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of objectIdList.")
         self.objectIdList.append(_val1)