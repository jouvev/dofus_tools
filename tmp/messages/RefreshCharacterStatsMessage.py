from tmp.types.GameFightCharacteristics import GameFightCharacteristics
class RefreshCharacterStatsMessage:
   def __init__(self,input):
      self._fighterIdFunc(input)
      self.stats = GameFightCharacteristics(input)
   
   def _fighterIdFunc(self,input) :
      self.fighterId = input.readDouble()
      if(self.fighterId < -9007199254740992 or self.fighterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.fighterId + ") on element of RefreshCharacterStatsMessage.fighterId.")