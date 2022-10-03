from tmp.types.HouseInstanceInformations import HouseInstanceInformations
from tmp.types.HouseInformations import HouseInformations
class HouseOnMapInformations(HouseInformations):
   def __init__(self,input):
      self.doorsOnMap = []
      self.houseInstances = []
      _val1 = 0
      _item2 = None
      super().__init__(input)
      _doorsOnMapLen = input.readUnsignedShort()
      for _i1 in range(0,_doorsOnMapLen):
         _val1 = input.readInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of doorsOnMap.")
         self.doorsOnMap.append(_val1)
      _houseInstancesLen = input.readUnsignedShort()
      for _i2 in range(0,_houseInstancesLen):
         _item2 = HouseInstanceInformations(input)
         self.houseInstances.append(_item2)