from src.reseau.messages.SelectedServerDataMessage import SelectedServerDataMessage
from src.reseau.types.GameServerInformations import GameServerInformations

class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
   def __init__(self,input):
      self.servers = []
      _item1 = None
      super().__init__(input)
      _serversLen = input.readUnsignedShort()
      for _i1 in range(0,_serversLen):
         _item1 = GameServerInformations(input)
         self.servers.append(_item1)

   def resume(self):
      super().resume()
      for e in self.servers:
         e.resume()
