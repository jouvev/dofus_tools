import src.reseau.TypesFactory as pf
from src.reseau.types.QuestActiveInformations import QuestActiveInformations

class QuestActiveDetailedInformations(QuestActiveInformations):
   def __init__(self,input):
      self.objectives = []
      _id2 = 0
      _item2 = None
      super().__init__(input)
      self._stepIdFunc(input)
      _objectivesLen = input.readUnsignedShort()
      for _i2 in range(0,_objectivesLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.objectives.append(_item2)
   
   def _stepIdFunc(self,input) :
      self.stepId = input.readVarUhShort()
      if(self.stepId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.stepId) + ") on element of QuestActiveDetailedInformations.stepId.")

   def resume(self):
      super().resume()
      print("stepId :",self.stepId)
      for e in self.objectives:
         e.resume()
