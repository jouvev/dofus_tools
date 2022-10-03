import tmp.TypesFactory as pf
from tmp.types.AccountTagInformation import AccountTagInformation
class BasicWhoIsMessage:
   def __init__(self,input):
      self.socialGroups = []
      _id10 = 0
      _item10 = None
      self.deserializeByteBoxes(input)
      self._positionFunc(input)
      self.accountTag = AccountTagInformation(input)
      self._accountIdFunc(input)
      self._playerNameFunc(input)
      self._playerIdFunc(input)
      self._areaIdFunc(input)
      self._serverIdFunc(input)
      self._originServerIdFunc(input)
      _socialGroupsLen = input.readUnsignedShort()
      for _i10 in range(0,_socialGroupsLen):
         _id10 = input.readUnsignedShort()
         _item10 = pf.TypesFactory.get_instance_id(_id10,input)
         self.socialGroups.append(_item10)
      self._playerStateFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.self = bool(bin(_box0)[2:].zfill(8)[0])
      self.verbose = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _positionFunc(self,input) :
      self.position = input.readByte()
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + self.accountId + ") on element of BasicWhoIsMessage.accountId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of BasicWhoIsMessage.playerId.")
   
   def _areaIdFunc(self,input) :
      self.areaId = input.readShort()
   
   def _serverIdFunc(self,input) :
      self.serverId = input.readShort()
   
   def _originServerIdFunc(self,input) :
      self.originServerId = input.readShort()
   
   def _playerStateFunc(self,input) :
      self.playerState = input.readByte()
      if(self.playerState < 0) :
         raise RuntimeError("Forbidden value (" + self.playerState + ") on element of BasicWhoIsMessage.playerState.")