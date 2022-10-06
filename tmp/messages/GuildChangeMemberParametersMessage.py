class GuildChangeMemberParametersMessage:
   def __init__(self,input):
      self._memberIdFunc(input)
      self._rankIdFunc(input)
      self._experienceGivenPercentFunc(input)
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.memberId) + ") on element of GuildChangeMemberParametersMessage.memberId.")
   
   def _rankIdFunc(self,input) :
      self.rankId = input.readVarUhInt()
      if(self.rankId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rankId) + ") on element of GuildChangeMemberParametersMessage.rankId.")
   
   def _experienceGivenPercentFunc(self,input) :
      self.experienceGivenPercent = input.readByte()
      if(self.experienceGivenPercent < 0 or self.experienceGivenPercent > 100) :
         raise RuntimeError("Forbidden value (" + str(self.experienceGivenPercent) + ") on element of GuildChangeMemberParametersMessage.experienceGivenPercent.")

   def resume(self):
      print("memberId :",self.memberId)
      print("rankId :",self.rankId)
      print("experienceGivenPercent :",self.experienceGivenPercent)
