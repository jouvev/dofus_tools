import src.reseau.TypesFactory as pf
from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.FriendInformations import FriendInformations

class FriendOnlineInformations(FriendInformations):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._levelFunc(input)
      self._alignmentSideFunc(input)
      self._breedFunc(input)
      self.guildInfo = GuildInformations(input)
      self._moodSmileyIdFunc(input)
      _id9 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id9,input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.sex = bool(bin(_box0)[2:].zfill(8)[0])
      self.havenBagShared = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of FriendOnlineInformations.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FriendOnlineInformations.level.")
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
      if(self.breed < 1 or self.breed > 18) :
         raise RuntimeError("Forbidden value (" + str(self.breed) + ") on element of FriendOnlineInformations.breed.")
   
   def _moodSmileyIdFunc(self,input) :
      self.moodSmileyId = input.readVarUhShort()
      if(self.moodSmileyId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.moodSmileyId) + ") on element of FriendOnlineInformations.moodSmileyId.")

   def resume(self):
      super().resume()
      print("playerId :",self.playerId)
      print("playerName :",self.playerName)
      print("level :",self.level)
      print("alignmentSide :",self.alignmentSide)
      print("breed :",self.breed)
      print("moodSmileyId :",self.moodSmileyId)
      self.guildInfo.resume()
