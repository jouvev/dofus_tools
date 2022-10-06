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
         raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element of MonsterInGroupLightInformations.grade.")
   
   def _levelFunc(self,input) :
      self.level = input.readShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of MonsterInGroupLightInformations.level.")

   def resume(self):
      print("genericId :",self.genericId)
      print("grade :",self.grade)
      print("level :",self.level)
