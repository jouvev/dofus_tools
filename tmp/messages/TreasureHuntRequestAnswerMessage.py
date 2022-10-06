class TreasureHuntRequestAnswerMessage:
   def __init__(self,input):
      self._questTypeFunc(input)
      self._resultFunc(input)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.questType) + ") on element of TreasureHuntRequestAnswerMessage.questType.")
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + str(self.result) + ") on element of TreasureHuntRequestAnswerMessage.result.")

   def resume(self):
      print("questType :",self.questType)
      print("result :",self.result)
