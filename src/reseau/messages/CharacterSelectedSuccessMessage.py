from src.reseau.types.CharacterBaseInformations import CharacterBaseInformations

class CharacterSelectedSuccessMessage:
   def __init__(self,input):
      self.infos = CharacterBaseInformations(input)
      self._isCollectingStatsFunc(input)
   
   def _isCollectingStatsFunc(self,input) :
      self.isCollectingStats = input.readBoolean()

   def resume(self):
      print("isCollectingStats :",self.isCollectingStats)
      self.infos.resume()
