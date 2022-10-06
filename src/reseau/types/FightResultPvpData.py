from src.reseau.types.FightResultAdditionalData import FightResultAdditionalData

class FightResultPvpData(FightResultAdditionalData):
   def __init__(self,input):
      super().__init__(input)
      self._gradeFunc(input)
      self._minHonorForGradeFunc(input)
      self._maxHonorForGradeFunc(input)
      self._honorFunc(input)
      self._honorDeltaFunc(input)
   
   def _gradeFunc(self,input) :
      self.grade = input.readUnsignedByte()
      if(self.grade < 0 or self.grade > 255) :
         raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element of FightResultPvpData.grade.")
   
   def _minHonorForGradeFunc(self,input) :
      self.minHonorForGrade = input.readVarUhShort()
      if(self.minHonorForGrade < 0 or self.minHonorForGrade > 20000) :
         raise RuntimeError("Forbidden value (" + str(self.minHonorForGrade) + ") on element of FightResultPvpData.minHonorForGrade.")
   
   def _maxHonorForGradeFunc(self,input) :
      self.maxHonorForGrade = input.readVarUhShort()
      if(self.maxHonorForGrade < 0 or self.maxHonorForGrade > 20000) :
         raise RuntimeError("Forbidden value (" + str(self.maxHonorForGrade) + ") on element of FightResultPvpData.maxHonorForGrade.")
   
   def _honorFunc(self,input) :
      self.honor = input.readVarUhShort()
      if(self.honor < 0 or self.honor > 20000) :
         raise RuntimeError("Forbidden value (" + str(self.honor) + ") on element of FightResultPvpData.honor.")
   
   def _honorDeltaFunc(self,input) :
      self.honorDelta = input.readVarShort()

   def resume(self):
      super().resume()
      print("grade :",self.grade)
      print("minHonorForGrade :",self.minHonorForGrade)
      print("maxHonorForGrade :",self.maxHonorForGrade)
      print("honor :",self.honor)
      print("honorDelta :",self.honorDelta)
