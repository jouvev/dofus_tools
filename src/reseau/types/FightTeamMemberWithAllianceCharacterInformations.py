from src.reseau.types.BasicAllianceInformations import BasicAllianceInformations
from src.reseau.types.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations

class FightTeamMemberWithAllianceCharacterInformations(FightTeamMemberCharacterInformations):
   def __init__(self,input):
      super().__init__(input)
      self.allianceInfos = BasicAllianceInformations(input)

   def resume(self):
      super().resume()
      self.allianceInfos.resum()
