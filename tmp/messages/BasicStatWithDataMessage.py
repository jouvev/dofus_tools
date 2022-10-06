import tmp.TypesFactory as pf
from tmp.messages.BasicStatMessage import BasicStatMessage

class BasicStatWithDataMessage(BasicStatMessage):
   def __init__(self,input):
      self.datas = []
      _id1 = 0
      _item1 = None
      super().__init__(input)
      _datasLen = input.readUnsignedShort()
      for _i1 in range(0,_datasLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.datas.append(_item1)

   def resume(self):
      super().resume()
      for e in self.datas:
         e.resume()
