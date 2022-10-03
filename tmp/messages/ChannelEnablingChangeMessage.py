class ChannelEnablingChangeMessage:
   def __init__(self,input):
      self._channelFunc(input)
      self._enableFunc(input)
   
   def _channelFunc(self,input) :
      self.channel = input.readByte()
      if(self.channel < 0) :
         raise RuntimeError("Forbidden value (" + self.channel + ") on element of ChannelEnablingChangeMessage.channel.")
   
   def _enableFunc(self,input) :
      self.enable = input.readBoolean()