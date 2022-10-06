from tmp.types.GuildRecruitmentInformation import GuildRecruitmentInformation

class RecruitmentInformationMessage:
   def __init__(self,input):
      self.recruitmentData = GuildRecruitmentInformation(input)

   def resume(self):
      self.recruitmentData.resum()
