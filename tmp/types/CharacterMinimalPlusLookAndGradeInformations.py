from tmp.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
class CharacterMinimalPlusLookAndGradeInformations(CharacterMinimalPlusLookInformations):
   def __init__(self,input):
      super().__init__(input)
      self._gradeFunc(input)
   
   def _gradeFunc(self,input) :
      self.grade = input.readVarUhInt()
      if(self.grade < 0) :
         raise RuntimeError("Forbidden value (" + self.grade + ") on element of CharacterMinimalPlusLookAndGradeInformations.grade.")