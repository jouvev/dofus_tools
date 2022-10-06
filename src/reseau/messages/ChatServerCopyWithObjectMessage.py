from src.reseau.messages.ChatServerCopyMessage import ChatServerCopyMessage
from src.reseau.types.ObjectItem import ObjectItem

class ChatServerCopyWithObjectMessage(ChatServerCopyMessage):
   def __init__(self,input):
      self.objects = []
      _item1 = None
      super().__init__(input)
      _objectsLen = input.readUnsignedShort()
      for _i1 in range(0,_objectsLen):
         _item1 = ObjectItem(input)
         self.objects.append(_item1)

   def resume(self):
      super().resume()
      for e in self.objects:
         e.resume()
