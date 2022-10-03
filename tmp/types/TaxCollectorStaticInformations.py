from tmp.types.GuildInformations import GuildInformations
class TaxCollectorStaticInformations:
   def __init__(self,input):
      self._firstNameIdFunc(input)
      self._lastNameIdFunc(input)
      self.guildIdentity = GuildInformations(input)
      self._callerIdFunc(input)
   
   def _firstNameIdFunc(self,input) :
      self.firstNameId = input.readVarUhShort()
      if(self.firstNameId < 0) :
         raise RuntimeError("Forbidden value (" + self.firstNameId + ") on element of TaxCollectorStaticInformations.firstNameId.")
   
   def _lastNameIdFunc(self,input) :
      self.lastNameId = input.readVarUhShort()
      if(self.lastNameId < 0) :
         raise RuntimeError("Forbidden value (" + self.lastNameId + ") on element of TaxCollectorStaticInformations.lastNameId.")
   
   def _callerIdFunc(self,input) :
      self.callerId = input.readVarUhLong()
      if(self.callerId < 0 or self.callerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.callerId + ") on element of TaxCollectorStaticInformations.callerId.")