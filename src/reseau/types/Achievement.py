from src.reseau.types.AchievementObjective import AchievementObjective
from src.reseau.types.AchievementStartedObjective import AchievementStartedObjective

class Achievement:
   def __init__(self,input):
      self.finishedObjective = []
      self.startedObjectives = []
      _item2 = None
      _item3 = None
      self._idFunc(input)
      _finishedObjectiveLen = input.readUnsignedShort()
      for _i2 in range(0,_finishedObjectiveLen):
         _item2 = AchievementObjective(input)
         self.finishedObjective.append(_item2)
      _startedObjectivesLen = input.readUnsignedShort()
      for _i3 in range(0,_startedObjectivesLen):
         _item3 = AchievementStartedObjective(input)
         self.startedObjectives.append(_item3)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhShort()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of Achievement.id.")

   def resume(self):
      print("id :",self.id)
      for e in self.finishedObjective:
         e.resume()
      for e in self.startedObjectives:
         e.resume()
