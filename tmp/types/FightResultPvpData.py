from tmp.types.FightResultAdditionalData import FightResultAdditionalData
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
         raise RuntimeError("Forbidden value (" + self.grade + ") on element of FightResultPvpData.grade.")
   
   def _minHonorForGradeFunc(self,input) :
      self.minHonorForGrade = input.readVarUhShort()
      if(self.minHonorForGrade < 0 or self.minHonorForGrade > 20000) :
         raise RuntimeError("Forbidden value (" + self.minHonorForGrade + ") on element of FightResultPvpData.minHonorForGrade.")
   
   def _maxHonorForGradeFunc(self,input) :
      self.maxHonorForGrade = input.readVarUhShort()
      if(self.maxHonorForGrade < 0 or self.maxHonorForGrade > 20000) :
         raise RuntimeError("Forbidden value (" + self.maxHonorForGrade + ") on element of FightResultPvpData.maxHonorForGrade.")
   
   def _honorFunc(self,input) :
      self.honor = input.readVarUhShort()
      if(self.honor < 0 or self.honor > 20000) :
         raise RuntimeError("Forbidden value (" + self.honor + ") on element of FightResultPvpData.honor.")
   
   def _honorDeltaFunc(self,input) :
      self.honorDelta = input.readVarShort()