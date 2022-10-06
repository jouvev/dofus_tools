from tmp.messages.ChatSmileyMessage import ChatSmileyMessage

class LocalizedChatSmileyMessage(ChatSmileyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._cellIdFunc(input)
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readVarUhShort()
      if(self.cellId < 0 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of LocalizedChatSmileyMessage.cellId.")

   def resume(self):
      super().resume()
      print("cellId :",self.cellId)
