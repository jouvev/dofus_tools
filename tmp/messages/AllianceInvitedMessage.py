from tmp.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations

class AllianceInvitedMessage:
   def __init__(self,input):
      self._recruterIdFunc(input)
      self._recruterNameFunc(input)
      self.allianceInfo = BasicNamedAllianceInformations(input)
   
   def _recruterIdFunc(self,input) :
      self.recruterId = input.readVarUhLong()
      if(self.recruterId < 0 or self.recruterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.recruterId) + ") on element of AllianceInvitedMessage.recruterId.")
   
   def _recruterNameFunc(self,input) :
      self.recruterName = input.readUTF()

   def resume(self):
      print("recruterId :",self.recruterId)
      print("recruterName :",self.recruterName)
      self.allianceInfo.resum()
