class AllianceModificationStartedMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.canChangeName = bool(bin(_box0)[2:].zfill(8)[0])
      self.canChangeTag = bool(bin(_box0)[2:].zfill(8)[1])
      self.canChangeEmblem = bool(bin(_box0)[2:].zfill(8)[2])

   def resume(self):
      pass