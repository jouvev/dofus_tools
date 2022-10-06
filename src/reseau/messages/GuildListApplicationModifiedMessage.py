from src.reseau.types.GuildApplicationInformation import GuildApplicationInformation

class GuildListApplicationModifiedMessage:
   def __init__(self,input):
      self.apply = GuildApplicationInformation(input)
      self._stateFunc(input)
      self._playerIdFunc(input)
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of GuildListApplicationModifiedMessage.state.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of GuildListApplicationModifiedMessage.playerId.")

   def resume(self):
      print("state :",self.state)
      print("playerId :",self.playerId)
      self.apply.resum()
