from tmp.messages.ChatServerMessage import ChatServerMessage

class ChatAdminServerMessage(ChatServerMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
