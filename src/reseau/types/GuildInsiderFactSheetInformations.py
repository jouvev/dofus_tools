from src.reseau.types.GuildFactSheetInformations import GuildFactSheetInformations

class GuildInsiderFactSheetInformations(GuildFactSheetInformations):
   def __init__(self,input):
      super().__init__(input)
      self._leaderNameFunc(input)
      self._nbConnectedMembersFunc(input)
      self._nbTaxCollectorsFunc(input)
   
   def _leaderNameFunc(self,input) :
      self.leaderName = input.readUTF()
   
   def _nbConnectedMembersFunc(self,input) :
      self.nbConnectedMembers = input.readVarUhShort()
      if(self.nbConnectedMembers < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbConnectedMembers) + ") on element of GuildInsiderFactSheetInformations.nbConnectedMembers.")
   
   def _nbTaxCollectorsFunc(self,input) :
      self.nbTaxCollectors = input.readByte()
      if(self.nbTaxCollectors < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbTaxCollectors) + ") on element of GuildInsiderFactSheetInformations.nbTaxCollectors.")

   def resume(self):
      super().resume()
      print("leaderName :",self.leaderName)
      print("nbConnectedMembers :",self.nbConnectedMembers)
      print("nbTaxCollectors :",self.nbTaxCollectors)
