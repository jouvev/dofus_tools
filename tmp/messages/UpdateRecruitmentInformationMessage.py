from tmp.types.GuildRecruitmentInformation import GuildRecruitmentInformation
class UpdateRecruitmentInformationMessage:
   def __init__(self,input):
      self.recruitmentData = GuildRecruitmentInformation(input)