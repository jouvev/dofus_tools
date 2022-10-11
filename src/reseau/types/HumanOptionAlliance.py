from src.reseau.types.AllianceInformations import AllianceInformations
from src.reseau.types.HumanOption import HumanOption

class HumanOptionAlliance(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self.allianceInformations = AllianceInformations(input)
      self._aggressableFunc(input)
   
   def _aggressableFunc(self,input) :
      self.aggressable = input.readByte()
      if(self.aggressable < 0) :
         raise RuntimeError("Forbidden value (" + str(self.aggressable) + ") on element of HumanOptionAlliance.aggressable.")

   def resume(self):
      super().resume()
      print("aggressable :",self.aggressable)
      self.allianceInformations.resume()
