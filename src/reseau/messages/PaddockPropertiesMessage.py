from src.reseau.types.PaddockInstancesInformations import PaddockInstancesInformations

class PaddockPropertiesMessage:
   def __init__(self,input):
      self.properties = PaddockInstancesInformations(input)

   def resume(self):
      self.properties.resume()
