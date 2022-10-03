class CinematicMessage:
   def __init__(self,input):
      self._cinematicIdFunc(input)
   
   def _cinematicIdFunc(self,input) :
      self.cinematicId = input.readVarUhShort()
      if(self.cinematicId < 0) :
         raise RuntimeError("Forbidden value (" + self.cinematicId + ") on element of CinematicMessage.cinematicId.")