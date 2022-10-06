from src.reseau.types.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer

class DungeonPartyFinderRoomContentMessage:
   def __init__(self,input):
      self.players = []
      _item2 = None
      self._dungeonIdFunc(input)
      _playersLen = input.readUnsignedShort()
      for _i2 in range(0,_playersLen):
         _item2 = DungeonPartyFinderPlayer(input)
         self.players.append(_item2)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dungeonId) + ") on element of DungeonPartyFinderRoomContentMessage.dungeonId.")

   def resume(self):
      print("dungeonId :",self.dungeonId)
      for e in self.players:
         e.resume()
