from tmp.types.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer

class DungeonPartyFinderRoomContentUpdateMessage:
   def __init__(self,input):
      self.addedPlayers = []
      self.removedPlayersIds = []
      _item2 = None
      _val3 = None
      self._dungeonIdFunc(input)
      _addedPlayersLen = input.readUnsignedShort()
      for _i2 in range(0,_addedPlayersLen):
         _item2 = DungeonPartyFinderPlayer(input)
         self.addedPlayers.append(_item2)
      _removedPlayersIdsLen = input.readUnsignedShort()
      for _i3 in range(0,_removedPlayersIdsLen):
         _val3 = input.readVarUhLong()
         if(_val3 < 0 or _val3 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of removedPlayersIds.")
         self.removedPlayersIds.append(_val3)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dungeonId) + ") on element of DungeonPartyFinderRoomContentUpdateMessage.dungeonId.")

   def resume(self):
      print("dungeonId :",self.dungeonId)
      for e in self.addedPlayers:
         e.resume()
      print("removedPlayersIds :",self.removedPlayersIds)
