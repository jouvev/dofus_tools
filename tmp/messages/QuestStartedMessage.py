class QuestStartedMessage:
   def __init__(self,input):
      self._questIdFunc(input)
   
   def _questIdFunc(self,input) :
      self.questId = input.readVarUhShort()
      if(self.questId < 0) :
         raise RuntimeError("Forbidden value (" + self.questId + ") on element of QuestStartedMessage.questId.")