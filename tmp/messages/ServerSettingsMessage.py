class ServerSettingsMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._langFunc(input)
      self._communityFunc(input)
      self._gameTypeFunc(input)
      self._arenaLeaveBanTimeFunc(input)
      self._itemMaxLevelFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.isMonoAccount = bool(bin(_box0)[2:].zfill(8)[0])
      self.hasFreeAutopilot = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _langFunc(self,input) :
      self.lang = input.readUTF()
   
   def _communityFunc(self,input) :
      self.community = input.readByte()
      if(self.community < 0) :
         raise RuntimeError("Forbidden value (" + self.community + ") on element of ServerSettingsMessage.community.")
   
   def _gameTypeFunc(self,input) :
      self.gameType = input.readByte()
   
   def _arenaLeaveBanTimeFunc(self,input) :
      self.arenaLeaveBanTime = input.readVarUhShort()
      if(self.arenaLeaveBanTime < 0) :
         raise RuntimeError("Forbidden value (" + self.arenaLeaveBanTime + ") on element of ServerSettingsMessage.arenaLeaveBanTime.")
   
   def _itemMaxLevelFunc(self,input) :
      self.itemMaxLevel = input.readInt()
      if(self.itemMaxLevel < 0) :
         raise RuntimeError("Forbidden value (" + self.itemMaxLevel + ") on element of ServerSettingsMessage.itemMaxLevel.")