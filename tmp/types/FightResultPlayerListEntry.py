import tmp.TypesFactory as pf
from tmp.types.FightResultFighterListEntry import FightResultFighterListEntry
class FightResultPlayerListEntry(FightResultFighterListEntry):
   def __init__(self,input):
      self.additional = []
      _id2 = 0
      _item2 = None
      super().__init__(input)
      self._levelFunc(input)
      _additionalLen = input.readUnsignedShort()
      for _i2 in range(0,_additionalLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.additional.append(_item2)
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of FightResultPlayerListEntry.level.")