from src.reseau.types.GuildInformations import GuildInformations

class GuildInAllianceInformations(GuildInformations):
   def __init__(self,input):
      super().__init__(input)
      self._nbMembersFunc(input)
      self._joinDateFunc(input)
   
   def _nbMembersFunc(self,input) :
      self.nbMembers = input.readUnsignedByte()
      if(self.nbMembers < 1 or self.nbMembers > 240) :
         raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element of GuildInAllianceInformations.nbMembers.")
   
   def _joinDateFunc(self,input) :
      self.joinDate = input.readInt()
      if(self.joinDate < 0) :
         raise RuntimeError("Forbidden value (" + str(self.joinDate) + ") on element of GuildInAllianceInformations.joinDate.")

   def resume(self):
      super().resume()
      print("nbMembers :",self.nbMembers)
      print("joinDate :",self.joinDate)
