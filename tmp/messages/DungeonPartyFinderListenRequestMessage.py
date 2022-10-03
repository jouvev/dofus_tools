class DungeonPartyFinderListenRequestMessage:
   def __init__(self,input):
      self._dungeonIdFunc(input)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + self.dungeonId + ") on element of DungeonPartyFinderListenRequestMessage.dungeonId.")