from tmp.types.BasicAllianceInformations import BasicAllianceInformations
from tmp.types.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
class FightTeamMemberWithAllianceCharacterInformations(FightTeamMemberCharacterInformations):
   def __init__(self,input):
      super().__init__(input)
      self.allianceInfos = BasicAllianceInformations(input)