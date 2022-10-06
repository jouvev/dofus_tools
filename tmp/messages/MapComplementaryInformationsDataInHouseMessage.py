from tmp.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from tmp.types.HouseInformationsInside import HouseInformationsInside

class MapComplementaryInformationsDataInHouseMessage(MapComplementaryInformationsDataMessage):
   def __init__(self,input):
      super().__init__(input)
      self.currentHouse = HouseInformationsInside(input)

   def resume(self):
      super().resume()
      self.currentHouse.resum()
