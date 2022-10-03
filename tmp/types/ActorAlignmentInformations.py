class ActorAlignmentInformations:
   def __init__(self,input):
      self._alignmentSideFunc(input)
      self._alignmentValueFunc(input)
      self._alignmentGradeFunc(input)
      self._characterPowerFunc(input)
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()
   
   def _alignmentValueFunc(self,input) :
      self.alignmentValue = input.readByte()
      if(self.alignmentValue < 0) :
         raise RuntimeError("Forbidden value (" + self.alignmentValue + ") on element of ActorAlignmentInformations.alignmentValue.")
   
   def _alignmentGradeFunc(self,input) :
      self.alignmentGrade = input.readByte()
      if(self.alignmentGrade < 0) :
         raise RuntimeError("Forbidden value (" + self.alignmentGrade + ") on element of ActorAlignmentInformations.alignmentGrade.")
   
   def _characterPowerFunc(self,input) :
      self.characterPower = input.readDouble()
      if(self.characterPower < -9007199254740992 or self.characterPower > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.characterPower + ") on element of ActorAlignmentInformations.characterPower.")