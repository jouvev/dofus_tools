from src.reseau.types.BasicGuildInformations import BasicGuildInformations
from src.reseau.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations

class CharacterMinimalGuildInformations(CharacterMinimalPlusLookInformations):
   def __init__(self,input):
      super().__init__(input)
      self.guild = BasicGuildInformations(input)

   def resume(self):
      super().resume()
      self.guild.resume()
