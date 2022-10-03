from tmp.types.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from tmp.types.BasicGuildInformations import BasicGuildInformations
class TaxCollectorAttackedResultMessage:
   def __init__(self,input):
      self._deadOrAliveFunc(input)
      self.basicInfos = TaxCollectorBasicInformations(input)
      self.guild = BasicGuildInformations(input)
   
   def _deadOrAliveFunc(self,input) :
      self.deadOrAlive = input.readBoolean()