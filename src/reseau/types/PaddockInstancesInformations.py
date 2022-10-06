import src.reseau.TypesFactory as pf
from src.reseau.types.PaddockInformations import PaddockInformations

class PaddockInstancesInformations(PaddockInformations):
   def __init__(self,input):
      self.paddocks = []
      _id1 = 0
      _item1 = None
      super().__init__(input)
      _paddocksLen = input.readUnsignedShort()
      for _i1 in range(0,_paddocksLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.paddocks.append(_item1)

   def resume(self):
      super().resume()
      for e in self.paddocks:
         e.resume()
