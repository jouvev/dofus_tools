from tmp.types.BasicAllianceInformations import BasicAllianceInformations
class BasicNamedAllianceInformations(BasicAllianceInformations):
   def __init__(self,input):
      super().__init__(input)
      self._allianceNameFunc(input)
   
   def _allianceNameFunc(self,input) :
      self.allianceName = input.readUTF()