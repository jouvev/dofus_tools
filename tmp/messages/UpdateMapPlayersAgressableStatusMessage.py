class UpdateMapPlayersAgressableStatusMessage:
   def __init__(self,input):
      self.playerIds = []
      self.enable = []
      _val1 = None
      _val2 = 0
      _playerIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_playerIdsLen):
         _val1 = input.readVarUhLong()
         if(_val1 < 0 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of playerIds.")
         self.playerIds.append(_val1)
      _enableLen = input.readUnsignedShort()
      for _i2 in range(0,_enableLen):
         _val2 = input.readByte()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of enable.")
         self.enable.append(_val2)