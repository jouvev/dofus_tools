class MonsterInGroupLightInformations:
   def __init__(self,input):
      self._genericIdFunc(input)
      self._gradeFunc(input)
      self._levelFunc(input)
   
   def _genericIdFunc(self,input) :
      self.genericId = input.readInt()
   
   def _gradeFunc(self,input) :
      self.grade = input.readByte()
      if(self.grade < 0) :
         raise RuntimeError("Forbidden value (" + self.grade + ") on element of MonsterInGroupLightInformations.grade.")
   
   def _levelFunc(self,input) :
      self.level = input.readShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of MonsterInGroupLightInformations.level.")