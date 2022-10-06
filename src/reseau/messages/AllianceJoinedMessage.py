from src.reseau.types.AllianceInformations import AllianceInformations

class AllianceJoinedMessage:
   def __init__(self,input):
      self.allianceInfo = AllianceInformations(input)
      self._enabledFunc(input)
      self._leadingGuildIdFunc(input)
   
   def _enabledFunc(self,input) :
      self.enabled = input.readBoolean()
   
   def _leadingGuildIdFunc(self,input) :
      self.leadingGuildId = input.readVarUhInt()
      if(self.leadingGuildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.leadingGuildId) + ") on element of AllianceJoinedMessage.leadingGuildId.")

   def resume(self):
      print("enabled :",self.enabled)
      print("leadingGuildId :",self.leadingGuildId)
      self.allianceInfo.resum()
