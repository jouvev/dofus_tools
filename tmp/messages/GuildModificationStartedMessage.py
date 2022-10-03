class GuildModificationStartedMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.canChangeName = bool(bin(_box0)[2:].zfill(8)[0])
      self.canChangeEmblem = bool(bin(_box0)[2:].zfill(8)[1])