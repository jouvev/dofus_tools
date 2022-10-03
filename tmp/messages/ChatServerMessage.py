from tmp.messages.ChatAbstractServerMessage import ChatAbstractServerMessage
class ChatServerMessage(ChatAbstractServerMessage):
   def __init__(self,input):
      super().__init__(input)
      self._senderIdFunc(input)
      self._senderNameFunc(input)
      self._prefixFunc(input)
      self._senderAccountIdFunc(input)
   
   def _senderIdFunc(self,input) :
      self.senderId = input.readDouble()
      if(self.senderId < -9007199254740992 or self.senderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.senderId + ") on element of ChatServerMessage.senderId.")
   
   def _senderNameFunc(self,input) :
      self.senderName = input.readUTF()
   
   def _prefixFunc(self,input) :
      self.prefix = input.readUTF()
   
   def _senderAccountIdFunc(self,input) :
      self.senderAccountId = input.readInt()
      if(self.senderAccountId < 0) :
         raise RuntimeError("Forbidden value (" + self.senderAccountId + ") on element of ChatServerMessage.senderAccountId.")