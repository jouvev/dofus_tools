from tmp.types.QuestObjectiveInformations import QuestObjectiveInformations

class QuestObjectiveInformationsWithCompletion(QuestObjectiveInformations):
   def __init__(self,input):
      super().__init__(input)
      self._curCompletionFunc(input)
      self._maxCompletionFunc(input)
   
   def _curCompletionFunc(self,input) :
      self.curCompletion = input.readVarUhShort()
      if(self.curCompletion < 0) :
         raise RuntimeError("Forbidden value (" + str(self.curCompletion) + ") on element of QuestObjectiveInformationsWithCompletion.curCompletion.")
   
   def _maxCompletionFunc(self,input) :
      self.maxCompletion = input.readVarUhShort()
      if(self.maxCompletion < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxCompletion) + ") on element of QuestObjectiveInformationsWithCompletion.maxCompletion.")

   def resume(self):
      super().resume()
      print("curCompletion :",self.curCompletion)
      print("maxCompletion :",self.maxCompletion)
