from tmp.types.GameFightFighterLightInformations import GameFightFighterLightInformations
class GameFightFighterNamedLightInformations(GameFightFighterLightInformations):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()