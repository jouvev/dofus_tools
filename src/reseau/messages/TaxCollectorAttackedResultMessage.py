from src.reseau.types.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from src.reseau.types.BasicGuildInformations import BasicGuildInformations

class TaxCollectorAttackedResultMessage:
   def __init__(self,input):
      self._deadOrAliveFunc(input)
      self.basicInfos = TaxCollectorBasicInformations(input)
      self.guild = BasicGuildInformations(input)
   
   def _deadOrAliveFunc(self,input) :
      self.deadOrAlive = input.readBoolean()

   def resume(self):
      print("deadOrAlive :",self.deadOrAlive)
      self.basicInfos.resume()
      self.guild.resume()
