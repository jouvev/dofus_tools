import src.reseau.TypesFactory as pf
from src.reseau.messages.ChatAbstractClientMessage import ChatAbstractClientMessage

class ChatClientPrivateMessage(ChatAbstractClientMessage):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.receiver = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      super().resume()
      self.receiver.resume()
