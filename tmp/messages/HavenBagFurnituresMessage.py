from tmp.types.HavenBagFurnitureInformation import HavenBagFurnitureInformation

class HavenBagFurnituresMessage:
   def __init__(self,input):
      self.furnituresInfos = []
      _item1 = None
      _furnituresInfosLen = input.readUnsignedShort()
      for _i1 in range(0,_furnituresInfosLen):
         _item1 = HavenBagFurnitureInformation(input)
         self.furnituresInfos.append(_item1)

   def resume(self):
      for e in self.furnituresInfos:
         e.resume()
