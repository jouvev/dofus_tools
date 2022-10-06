class QuestStepValidatedMessage:
   def __init__(self,input):
      self._questIdFunc(input)
      self._stepIdFunc(input)
   
   def _questIdFunc(self,input) :
      self.questId = input.readVarUhShort()
      if(self.questId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.questId) + ") on element of QuestStepValidatedMessage.questId.")
   
   def _stepIdFunc(self,input) :
      self.stepId = input.readVarUhShort()
      if(self.stepId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.stepId) + ") on element of QuestStepValidatedMessage.stepId.")

   def resume(self):
      print("questId :",self.questId)
      print("stepId :",self.stepId)
