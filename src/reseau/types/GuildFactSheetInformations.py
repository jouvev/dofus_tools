from src.reseau.types.GuildRecruitmentInformation import GuildRecruitmentInformation
from src.reseau.types.GuildInformations import GuildInformations

class GuildFactSheetInformations(GuildInformations):
   def __init__(self,input):
      super().__init__(input)
      self._leaderIdFunc(input)
      self._nbMembersFunc(input)
      self._lastActivityDayFunc(input)
      self.recruitment = GuildRecruitmentInformation(input)
      self._nbPendingApplyFunc(input)
   
   def _leaderIdFunc(self,input) :
      self.leaderId = input.readVarUhLong()
      if(self.leaderId < 0 or self.leaderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element of GuildFactSheetInformations.leaderId.")
   
   def _nbMembersFunc(self,input) :
      self.nbMembers = input.readVarUhShort()
      if(self.nbMembers < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element of GuildFactSheetInformations.nbMembers.")
   
   def _lastActivityDayFunc(self,input) :
      self.lastActivityDay = input.readShort()
      if(self.lastActivityDay < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastActivityDay) + ") on element of GuildFactSheetInformations.lastActivityDay.")
   
   def _nbPendingApplyFunc(self,input) :
      self.nbPendingApply = input.readInt()
      if(self.nbPendingApply < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbPendingApply) + ") on element of GuildFactSheetInformations.nbPendingApply.")

   def resume(self):
      super().resume()
      print("leaderId :",self.leaderId)
      print("nbMembers :",self.nbMembers)
      print("lastActivityDay :",self.lastActivityDay)
      print("nbPendingApply :",self.nbPendingApply)
      self.recruitment.resum()
