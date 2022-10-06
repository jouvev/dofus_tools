from src.reseau.types.GuildVersatileInformations import GuildVersatileInformations

class GuildInAllianceVersatileInformations(GuildVersatileInformations):
   def __init__(self,input):
      super().__init__(input)
      self._allianceIdFunc(input)
   
   def _allianceIdFunc(self,input) :
      self.allianceId = input.readVarUhInt()
      if(self.allianceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element of GuildInAllianceVersatileInformations.allianceId.")

   def resume(self):
      super().resume()
      print("allianceId :",self.allianceId)
