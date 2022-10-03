class TreasureHuntGiveUpRequestMessage:
   def __init__(self,input):
      self._questTypeFunc(input)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + self.questType + ") on element of TreasureHuntGiveUpRequestMessage.questType.")