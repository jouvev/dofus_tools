from src.reseau.types.AllianceInformations import AllianceInformations

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
         raise RuntimeError("Forbidden value (" + str(self.creationDate) + ") on element of AllianceFactSheetInformations.creationDate.")
   
   def _nbGuildsFunc(self,input) :
      self.nbGuilds = input.readVarUhShort()
      if(self.nbGuilds < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbGuilds) + ") on element of AllianceFactSheetInformations.nbGuilds.")
   
   def _nbMembersFunc(self,input) :
      self.nbMembers = input.readVarUhShort()
      if(self.nbMembers < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element of AllianceFactSheetInformations.nbMembers.")
   
   def _nbSubareaFunc(self,input) :
      self.nbSubarea = input.readVarUhShort()
      if(self.nbSubarea < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbSubarea) + ") on element of AllianceFactSheetInformations.nbSubarea.")

   def resume(self):
      super().resume()
      print("creationDate :",self.creationDate)
      print("nbGuilds :",self.nbGuilds)
      print("nbMembers :",self.nbMembers)
      print("nbSubarea :",self.nbSubarea)
