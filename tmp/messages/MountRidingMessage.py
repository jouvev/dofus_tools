class MountRidingMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.isRiding = bool(bin(_box0)[2:].zfill(8)[0])
      self.isAutopilot = bool(bin(_box0)[2:].zfill(8)[1])

   def resume(self):
      pass