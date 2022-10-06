from tmp.messages.TreasureHuntDigRequestAnswerMessage import TreasureHuntDigRequestAnswerMessage

class TreasureHuntDigRequestAnswerFailedMessage(TreasureHuntDigRequestAnswerMessage):
   def __init__(self,input):
      super().__init__(input)
      self._wrongFlagCountFunc(input)
   
   def _wrongFlagCountFunc(self,input) :
      self.wrongFlagCount = input.readByte()
      if(self.wrongFlagCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.wrongFlagCount) + ") on element of TreasureHuntDigRequestAnswerFailedMessage.wrongFlagCount.")

   def resume(self):
      super().resume()
      print("wrongFlagCount :",self.wrongFlagCount)
