from tmp.types.AbstractSocialGroupInfos import AbstractSocialGroupInfos
class BasicAllianceInformations(AbstractSocialGroupInfos):
   def __init__(self,input):
      super().__init__(input)
      self._allianceIdFunc(input)
      self._allianceTagFunc(input)
   
   def _allianceIdFunc(self,input) :
      self.allianceId = input.readVarUhInt()
      if(self.allianceId < 0) :
         raise RuntimeError("Forbidden value (" + self.allianceId + ") on element of BasicAllianceInformations.allianceId.")
   
   def _allianceTagFunc(self,input) :
      self.allianceTag = input.readUTF()