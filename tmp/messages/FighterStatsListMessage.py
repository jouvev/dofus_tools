from tmp.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations

class FighterStatsListMessage:
   def __init__(self,input):
      self.stats = CharacterCharacteristicsInformations(input)

   def resume(self):
      self.stats.resum()
