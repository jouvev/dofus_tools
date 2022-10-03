from tmp.types.AllianceInformations import AllianceInformations
class AllianceFactSheetInformations(AllianceInformations):
   def __init__(self,input):
      super().__init__(input)
      self._creationDateFunc(input)
      self._nbGuildsFunc(input)
      self._nbMembersFunc(input)
      self._nbSubareaFunc(input)
   
   def _creationDateFunc(self,input) :
      self.creationDate = input.readInt()
      if(self.creationDate < 0) :
         raise RuntimeError("Forbidden value (" + self.creationDate + ") on element of AllianceFactSheetInformations.creationDate.")
   
   def _nbGuildsFunc(self,input) :
      self.nbGuilds = input.readVarUhShort()
      if(self.nbGuilds < 0) :
         raise RuntimeError("Forbidden value (" + self.nbGuilds + ") on element of AllianceFactSheetInformations.nbGuilds.")
   
   def _nbMembersFunc(self,input) :
      self.nbMembers = input.readVarUhShort()
      if(self.nbMembers < 0) :
         raise RuntimeError("Forbidden value (" + self.nbMembers + ") on element of AllianceFactSheetInformations.nbMembers.")
   
   def _nbSubareaFunc(self,input) :
      self.nbSubarea = input.readVarUhShort()
      if(self.nbSubarea < 0) :
         raise RuntimeError("Forbidden value (" + self.nbSubarea + ") on element of AllianceFactSheetInformations.nbSubarea.")