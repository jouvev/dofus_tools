class TreasureHuntFlagRemoveRequestMessage:
   def __init__(self,input):
      self._questTypeFunc(input)
      self._indexFunc(input)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + self.questType + ") on element of TreasureHuntFlagRemoveRequestMessage.questType.")
   
   def _indexFunc(self,input) :
      self.index = input.readByte()
      if(self.index < 0) :
         raise RuntimeError("Forbidden value (" + self.index + ") on element of TreasureHuntFlagRemoveRequestMessage.index.")