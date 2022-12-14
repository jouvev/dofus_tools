from src.reseau.types.GameServerInformations import GameServerInformations

class ServersListMessage:
   def __init__(self,input):
      self.servers = []
      _item1 = None
      _serversLen = input.readUnsignedShort()
      for _i1 in range(0,_serversLen):
         _item1 = GameServerInformations(input)
         self.servers.append(_item1)
      self._canCreateNewCharacterFunc(input)
   
   def _canCreateNewCharacterFunc(self,input) :
      self.canCreateNewCharacter = input.readBoolean()

   def resume(self):
      print("canCreateNewCharacter :",self.canCreateNewCharacter)
      for e in self.servers:
         e.resume()
