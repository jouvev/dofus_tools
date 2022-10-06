import tmp.TypesFactory as pf

class AbstractTaxCollectorListMessage:
   def __init__(self,input):
      self.informations = []
      _id1 = 0
      _item1 = None
      _informationsLen = input.readUnsignedShort()
      for _i1 in range(0,_informationsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.informations.append(_item1)

   def resume(self):
      for e in self.informations:
         e.resume()
