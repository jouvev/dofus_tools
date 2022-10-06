from src.reseau.messages.ChatServerMessage import ChatServerMessage

class ChatKolizeumServerMessage(ChatServerMessage):
   def __init__(self,input):
      super().__init__(input)
      self._originServerIdFunc(input)
   
   def _originServerIdFunc(self,input) :
      self.originServerId = input.readShort()

   def resume(self):
      super().resume()
      print("originServerId :",self.originServerId)
