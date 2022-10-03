class UnfollowQuestObjectiveRequestMessage:
   def __init__(self,input):
      self._questIdFunc(input)
      self._objectiveIdFunc(input)
   
   def _questIdFunc(self,input) :
      self.questId = input.readVarUhShort()
      if(self.questId < 0) :
         raise RuntimeError("Forbidden value (" + self.questId + ") on element of UnfollowQuestObjectiveRequestMessage.questId.")
   
   def _objectiveIdFunc(self,input) :
      self.objectiveId = input.readShort()