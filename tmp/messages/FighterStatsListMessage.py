from tmp.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
class FighterStatsListMessage:
   def __init__(self,input):
      self.stats = CharacterCharacteristicsInformations(input)