import tmp.TypesFactory as pf
from tmp.messages.ChatAbstractClientMessage import ChatAbstractClientMessage
class ChatClientPrivateMessage(ChatAbstractClientMessage):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.receiver = pf.TypesFactory.get_instance_id(_id1,input)