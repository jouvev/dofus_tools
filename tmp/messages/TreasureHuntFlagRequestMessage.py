class TreasureHuntFlagRequestMessage:
   def __init__(self,input):
      self._questTypeFunc(input)
      self._indexFunc(input)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.questType) + ") on element of TreasureHuntFlagRequestMessage.questType.")
   
   def _indexFunc(self,input) :
      self.index = input.readByte()
      if(self.index < 0) :
         raise RuntimeError("Forbidden value (" + str(self.index) + ") on element of TreasureHuntFlagRequestMessage.index.")

   def resume(self):
      print("questType :",self.questType)
      print("index :",self.index)
