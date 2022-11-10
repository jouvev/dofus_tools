import src.reseau.TypesFactory as pf

class MapRunningFightDetailsMessage:
   def __init__(self,input):
      self.attackers = []
      self.defenders = []
      _id2 = 0
      _item2 = None
      _id3 = 0
      _item3 = None
      self._fightIdFunc(input)
      _attackersLen = input.readUnsignedShort()
      for _i2 in range(0,_attackersLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.attackers.append(_item2)
      _defendersLen = input.readUnsignedShort()
      for _i3 in range(0,_defendersLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.defenders.append(_item3)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of MapRunningFightDetailsMessage.fightId.")

   def resume(self):
      print("fightId :",self.fightId)
      for e in self.attackers:
         e.resume()
      for e in self.defenders:
         e.resume()
