from tmp.types.ActorAlignmentInformations import ActorAlignmentInformations
from tmp.types.GameFightFighterNamedInformations import GameFightFighterNamedInformations
class GameFightCharacterInformations(GameFightFighterNamedInformations):
   def __init__(self,input):
      super().__init__(input)
      self._levelFunc(input)
      self.alignmentInfos = ActorAlignmentInformations(input)
      self._breedFunc(input)
      self._sexFunc(input)
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of GameFightCharacterInformations.level.")
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()