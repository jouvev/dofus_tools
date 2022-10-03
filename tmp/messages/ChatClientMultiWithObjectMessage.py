from tmp.messages.ChatClientMultiMessage import ChatClientMultiMessage
from tmp.types.ObjectItem import ObjectItem
class ChatClientMultiWithObjectMessage(ChatClientMultiMessage):
   def __init__(self,input):
      self.objects = []
      _item1 = None
      super().__init__(input)
      _objectsLen = input.readUnsignedShort()
      for _i1 in range(0,_objectsLen):
         _item1 = ObjectItem(input)
         self.objects.append(_item1)