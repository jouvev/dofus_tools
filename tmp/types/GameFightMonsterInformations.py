from tmp.types.GameFightAIInformations import GameFightAIInformations

class GameFightMonsterInformations(GameFightAIInformations):
   def __init__(self,input):
      super().__init__(input)
      self._creatureGenericIdFunc(input)
      self._creatureGradeFunc(input)
      self._creatureLevelFunc(input)
   
   def _creatureGenericIdFunc(self,input) :
      self.creatureGenericId = input.readVarUhShort()
      if(self.creatureGenericId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.creatureGenericId) + ") on element of GameFightMonsterInformations.creatureGenericId.")
   
   def _creatureGradeFunc(self,input) :
      self.creatureGrade = input.readByte()
      if(self.creatureGrade < 0) :
         raise RuntimeError("Forbidden value (" + str(self.creatureGrade) + ") on element of GameFightMonsterInformations.creatureGrade.")
   
   def _creatureLevelFunc(self,input) :
      self.creatureLevel = input.readShort()
      if(self.creatureLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.creatureLevel) + ") on element of GameFightMonsterInformations.creatureLevel.")

   def resume(self):
      super().resume()
      print("creatureGenericId :",self.creatureGenericId)
      print("creatureGrade :",self.creatureGrade)
      print("creatureLevel :",self.creatureLevel)
