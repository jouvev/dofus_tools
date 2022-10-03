class QuestObjectiveValidationMessage:
   def __init__(self,input):
      self._questIdFunc(input)
      self._objectiveIdFunc(input)
   
   def _questIdFunc(self,input) :
      self.questId = input.readVarUhShort()
      if(self.questId < 0) :
         raise RuntimeError("Forbidden value (" + self.questId + ") on element of QuestObjectiveValidationMessage.questId.")
   
   def _objectiveIdFunc(self,input) :
      self.objectiveId = input.readVarUhShort()
      if(self.objectiveId < 0) :
         raise RuntimeError("Forbidden value (" + self.objectiveId + ") on element of QuestObjectiveValidationMessage.objectiveId.")