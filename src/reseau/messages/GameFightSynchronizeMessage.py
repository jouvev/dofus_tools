import src.reseau.TypesFactory as pf

class GameFightSynchronizeMessage:
   def __init__(self,input):
      self.fighters = []
      _id1 = 0
      _item1 = None
      _fightersLen = input.readUnsignedShort()
      for _i1 in range(0,_fightersLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.fighters.append(_item1)

   def resume(self):
      for e in self.fighters:
         e.resume()
