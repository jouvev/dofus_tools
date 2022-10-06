class ChatAbstractServerMessage:
   def __init__(self,input):
      self._channelFunc(input)
      self._contentFunc(input)
      self._timestampFunc(input)
      self._fingerprintFunc(input)
   
   def _channelFunc(self,input) :
      self.channel = input.readByte()
      if(self.channel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.channel) + ") on element of ChatAbstractServerMessage.channel.")
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()
   
   def _timestampFunc(self,input) :
      self.timestamp = input.readInt()
      if(self.timestamp < 0) :
         raise RuntimeError("Forbidden value (" + str(self.timestamp) + ") on element of ChatAbstractServerMessage.timestamp.")
   
   def _fingerprintFunc(self,input) :
      self.fingerprint = input.readUTF()

   def resume(self):
      print("channel :",self.channel)
      print("content :",self.content)
      print("timestamp :",self.timestamp)
      print("fingerprint :",self.fingerprint)
