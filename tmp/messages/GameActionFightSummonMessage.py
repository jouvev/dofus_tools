import tmp.TypesFactory as pf
from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightSummonMessage(AbstractGameActionMessage):
   def __init__(self,input):
      self.summons = []
      _id1 = 0
      _item1 = None
      super().__init__(input)
      _summonsLen = input.readUnsignedShort()
      for _i1 in range(0,_summonsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.summons.append(_item1)

   def resume(self):
      super().resume()
      for e in self.summons:
         e.resume()
