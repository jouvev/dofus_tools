from src.reseau.types.ActorAlignmentInformations import ActorAlignmentInformations

class ActorExtendedAlignmentInformations(ActorAlignmentInformations):
   def __init__(self,input):
      super().__init__(input)
      self._honorFunc(input)
      self._honorGradeFloorFunc(input)
      self._honorNextGradeFloorFunc(input)
      self._aggressableFunc(input)
   
   def _honorFunc(self,input) :
      self.honor = input.readVarUhShort()
      if(self.honor < 0 or self.honor > 20000) :
         raise RuntimeError("Forbidden value (" + str(self.honor) + ") on element of ActorExtendedAlignmentInformations.honor.")
   
   def _honorGradeFloorFunc(self,input) :
      self.honorGradeFloor = input.readVarUhShort()
      if(self.honorGradeFloor < 0 or self.honorGradeFloor > 20000) :
         raise RuntimeError("Forbidden value (" + str(self.honorGradeFloor) + ") on element of ActorExtendedAlignmentInformations.honorGradeFloor.")
   
   def _honorNextGradeFloorFunc(self,input) :
      self.honorNextGradeFloor = input.readVarUhShort()
      if(self.honorNextGradeFloor < 0 or self.honorNextGradeFloor > 20000) :
         raise RuntimeError("Forbidden value (" + str(self.honorNextGradeFloor) + ") on element of ActorExtendedAlignmentInformations.honorNextGradeFloor.")
   
   def _aggressableFunc(self,input) :
      self.aggressable = input.readByte()
      if(self.aggressable < 0) :
         raise RuntimeError("Forbidden value (" + str(self.aggressable) + ") on element of ActorExtendedAlignmentInformations.aggressable.")

   def resume(self):
      super().resume()
      print("honor :",self.honor)
      print("honorGradeFloor :",self.honorGradeFloor)
      print("honorNextGradeFloor :",self.honorNextGradeFloor)
      print("aggressable :",self.aggressable)
