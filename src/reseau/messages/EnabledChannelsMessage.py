class EnabledChannelsMessage:
   def __init__(self,input):
      self.channels = []
      self.disallowed = []
      _val1 = 0
      _val2 = 0
      _channelsLen = input.readUnsignedShort()
      for _i1 in range(0,_channelsLen):
         _val1 = input.readByte()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of channels.")
         self.channels.append(_val1)
      _disallowedLen = input.readUnsignedShort()
      for _i2 in range(0,_disallowedLen):
         _val2 = input.readByte()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of disallowed.")
         self.disallowed.append(_val2)

   def resume(self):
      print("channels :",self.channels)
      print("disallowed :",self.disallowed)
