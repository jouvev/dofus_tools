from tmp.messages.ChatAbstractClientMessage import ChatAbstractClientMessage
class ChatClientMultiMessage(ChatAbstractClientMessage):
   def __init__(self,input):
      super().__init__(input)
      self._channelFunc(input)
   
   def _channelFunc(self,input) :
      self.channel = input.readByte()
      if(self.channel < 0) :
         raise RuntimeError("Forbidden value (" + self.channel + ") on element of ChatClientMultiMessage.channel.")