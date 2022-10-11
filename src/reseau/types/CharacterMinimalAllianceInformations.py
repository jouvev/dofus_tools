from src.reseau.types.BasicAllianceInformations import BasicAllianceInformations
from src.reseau.types.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations

class CharacterMinimalAllianceInformations(CharacterMinimalGuildInformations):
   def __init__(self,input):
      super().__init__(input)
      self.alliance = BasicAllianceInformations(input)

   def resume(self):
      super().resume()
      self.alliance.resume()
