class GameContextRemoveMultipleElementsMessage:
   def __init__(self,input):
      self.elementsIds = []
      _val1 = None
      _elementsIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_elementsIdsLen):
         _val1 = input.readDouble()
         if(_val1 < -9007199254740992 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of elementsIds.")
         self.elementsIds.append(_val1)