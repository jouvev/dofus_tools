from src.reseau.messages.ChatAbstractClientMessage import ChatAbstractClientMessage

class ChatClientMultiMessage(ChatAbstractClientMessage):
   def __init__(self,input):
      super().__init__(input)
      self._channelFunc(input)
   
   def _channelFunc(self,input) :
      self.channel = input.readByte()
      if(self.channel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.channel) + ") on element of ChatClientMultiMessage.channel.")

   def resume(self):
      super().resume()
      print("channel :",self.channel)
