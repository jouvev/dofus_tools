from tmp.types.BasicAllianceInformations import BasicAllianceInformations
from tmp.types.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
class CharacterMinimalAllianceInformations(CharacterMinimalGuildInformations):
   def __init__(self,input):
      super().__init__(input)
      self.alliance = BasicAllianceInformations(input)