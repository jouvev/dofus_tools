from tmp.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
class CharacterStatsListMessage:
   def __init__(self,input):
      self.stats = CharacterCharacteristicsInformations(input)