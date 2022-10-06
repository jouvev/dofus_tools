from tmp.messages.GameContextRemoveElementMessage import GameContextRemoveElementMessage

class GameContextRemoveElementWithEventMessage(GameContextRemoveElementMessage):
   def __init__(self,input):
      super().__init__(input)
      self._elementEventIdFunc(input)
   
   def _elementEventIdFunc(self,input) :
      self.elementEventId = input.readByte()
      if(self.elementEventId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.elementEventId) + ") on element of GameContextRemoveElementWithEventMessage.elementEventId.")

   def resume(self):
      super().resume()
      print("elementEventId :",self.elementEventId)
