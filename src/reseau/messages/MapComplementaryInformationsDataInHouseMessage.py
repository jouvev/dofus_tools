from src.reseau.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from src.reseau.types.HouseInformationsInside import HouseInformationsInside

class MapComplementaryInformationsDataInHouseMessage(MapComplementaryInformationsDataMessage):
   def __init__(self,input):
      super().__init__(input)
      self.currentHouse = HouseInformationsInside(input)

   def resume(self):
      super().resume()
      self.currentHouse.resume()
