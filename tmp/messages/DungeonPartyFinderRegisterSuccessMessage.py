class DungeonPartyFinderRegisterSuccessMessage:
   def __init__(self,input):
      self.dungeonIds = []
      _val1 = 0
      _dungeonIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_dungeonIdsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of dungeonIds.")
         self.dungeonIds.append(_val1)

   def resume(self):
      print("dungeonIds :",self.dungeonIds)
