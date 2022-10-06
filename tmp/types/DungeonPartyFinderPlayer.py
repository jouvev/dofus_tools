class DungeonPartyFinderPlayer:
   def __init__(self,input):
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
      self._levelFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of DungeonPartyFinderPlayer.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
      if(self.breed < 1 or self.breed > 18) :
         raise RuntimeError("Forbidden value (" + str(self.breed) + ") on element of DungeonPartyFinderPlayer.breed.")
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of DungeonPartyFinderPlayer.level.")

   def resume(self):
      print("playerId :",self.playerId)
      print("playerName :",self.playerName)
      print("breed :",self.breed)
      print("sex :",self.sex)
      print("level :",self.level)
