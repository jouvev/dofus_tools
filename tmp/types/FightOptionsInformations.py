class FightOptionsInformations:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.isSecret = bool(bin(_box0)[2:].zfill(8)[0])
      self.isRestrictedToPartyOnly = bool(bin(_box0)[2:].zfill(8)[1])
      self.isClosed = bool(bin(_box0)[2:].zfill(8)[2])
      self.isAskingForHelp = bool(bin(_box0)[2:].zfill(8)[3])