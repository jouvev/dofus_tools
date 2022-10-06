class TrustStatusMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.trusted = bool(bin(_box0)[2:].zfill(8)[0])
      self.certified = bool(bin(_box0)[2:].zfill(8)[1])

   def resume(self):
      pass