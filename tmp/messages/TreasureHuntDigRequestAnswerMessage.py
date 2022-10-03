class TreasureHuntDigRequestAnswerMessage:
   def __init__(self,input):
      self._questTypeFunc(input)
      self._resultFunc(input)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + self.questType + ") on element of TreasureHuntDigRequestAnswerMessage.questType.")
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + self.result + ") on element of TreasureHuntDigRequestAnswerMessage.result.")