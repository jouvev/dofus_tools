from tmp.types.IgnoredInformations import IgnoredInformations
class IgnoredOnlineInformations(IgnoredInformations):
   def __init__(self,input):
      super().__init__(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of IgnoredOnlineInformations.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
      if(self.breed < 0 or self.breed > 18) :
         raise RuntimeError("Forbidden value (" + self.breed + ") on element of IgnoredOnlineInformations.breed.")
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()