import tmp.TypesFactory as pf

class AcquaintancesListMessage:
   def __init__(self,input):
      self.acquaintanceList = []
      _id1 = 0
      _item1 = None
      _acquaintanceListLen = input.readUnsignedShort()
      for _i1 in range(0,_acquaintanceListLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.acquaintanceList.append(_item1)

   def resume(self):
      for e in self.acquaintanceList:
         e.resume()
