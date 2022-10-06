class TreasureHuntFlagRequestAnswerMessage:
   def __init__(self,input):
      self._questTypeFunc(input)
      self._resultFunc(input)
      self._indexFunc(input)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.questType) + ") on element of TreasureHuntFlagRequestAnswerMessage.questType.")
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + str(self.result) + ") on element of TreasureHuntFlagRequestAnswerMessage.result.")
   
   def _indexFunc(self,input) :
      self.index = input.readByte()
      if(self.index < 0) :
         raise RuntimeError("Forbidden value (" + str(self.index) + ") on element of TreasureHuntFlagRequestAnswerMessage.index.")

   def resume(self):
      print("questType :",self.questType)
      print("result :",self.result)
      print("index :",self.index)
