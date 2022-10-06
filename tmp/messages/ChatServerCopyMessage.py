from tmp.messages.ChatAbstractServerMessage import ChatAbstractServerMessage

class ChatServerCopyMessage(ChatAbstractServerMessage):
   def __init__(self,input):
      super().__init__(input)
      self._receiverIdFunc(input)
      self._receiverNameFunc(input)
   
   def _receiverIdFunc(self,input) :
      self.receiverId = input.readVarUhLong()
      if(self.receiverId < 0 or self.receiverId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.receiverId) + ") on element of ChatServerCopyMessage.receiverId.")
   
   def _receiverNameFunc(self,input) :
      self.receiverName = input.readUTF()

   def resume(self):
      super().resume()
      print("receiverId :",self.receiverId)
      print("receiverName :",self.receiverName)
