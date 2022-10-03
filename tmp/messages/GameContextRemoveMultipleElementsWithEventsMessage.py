from tmp.messages.GameContextRemoveMultipleElementsMessage import GameContextRemoveMultipleElementsMessage
class GameContextRemoveMultipleElementsWithEventsMessage(GameContextRemoveMultipleElementsMessage):
   def __init__(self,input):
      self.elementEventIds = []
      _val1 = 0
      super().__init__(input)
      _elementEventIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_elementEventIdsLen):
         _val1 = input.readByte()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of elementEventIds.")
         self.elementEventIds.append(_val1)