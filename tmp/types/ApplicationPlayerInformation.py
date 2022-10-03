from tmp.types.PlayerStatus import PlayerStatus
class ApplicationPlayerInformation:
   def __init__(self,input):
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
      self._levelFunc(input)
      self._accountIdFunc(input)
      self._accountTagFunc(input)
      self._accountNicknameFunc(input)
      self.status = PlayerStatus(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of ApplicationPlayerInformation.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
      if(self.breed < 0 or self.breed > 18) :
         raise RuntimeError("Forbidden value (" + self.breed + ") on element of ApplicationPlayerInformation.breed.")
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhInt()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of ApplicationPlayerInformation.level.")
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readVarUhInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + self.accountId + ") on element of ApplicationPlayerInformation.accountId.")
   
   def _accountTagFunc(self,input) :
      self.accountTag = input.readUTF()
   
   def _accountNicknameFunc(self,input) :
      self.accountNickname = input.readUTF()