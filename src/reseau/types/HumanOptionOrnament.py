from src.reseau.types.HumanOption import HumanOption

class HumanOptionOrnament(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self._ornamentIdFunc(input)
      self._levelFunc(input)
      self._leagueIdFunc(input)
      self._ladderPositionFunc(input)
   
   def _ornamentIdFunc(self,input) :
      self.ornamentId = input.readVarUhShort()
      if(self.ornamentId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.ornamentId) + ") on element of HumanOptionOrnament.ornamentId.")
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of HumanOptionOrnament.level.")
   
   def _leagueIdFunc(self,input) :
      self.leagueId = input.readVarShort()
   
   def _ladderPositionFunc(self,input) :
      self.ladderPosition = input.readInt()

   def resume(self):
      super().resume()
      print("ornamentId :",self.ornamentId)
      print("level :",self.level)
      print("leagueId :",self.leagueId)
      print("ladderPosition :",self.ladderPosition)
