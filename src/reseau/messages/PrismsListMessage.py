import src.reseau.TypesFactory as pf

class PrismsListMessage:
   def __init__(self,input):
      self.prisms = []
      _id1 = 0
      _item1 = None
      _prismsLen = input.readUnsignedShort()
      for _i1 in range(0,_prismsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.prisms.append(_item1)

   def resume(self):
      for e in self.prisms:
         e.resume()
