from tmp.types.BasicGuildInformations import BasicGuildInformations
from tmp.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
class CharacterMinimalGuildInformations(CharacterMinimalPlusLookInformations):
   def __init__(self,input):
      super().__init__(input)
      self.guild = BasicGuildInformations(input)