from tmp.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations
class MapComplementaryInformationsDataInHavenBagMessage(MapComplementaryInformationsDataMessage):
   def __init__(self,input):
      super().__init__(input)
      self.ownerInformations = CharacterMinimalInformations(input)
      self._themeFunc(input)
      self._roomIdFunc(input)
      self._maxRoomIdFunc(input)
   
   def _themeFunc(self,input) :
      self.theme = input.readByte()
   
   def _roomIdFunc(self,input) :
      self.roomId = input.readByte()
      if(self.roomId < 0) :
         raise RuntimeError("Forbidden value (" + self.roomId + ") on element of MapComplementaryInformationsDataInHavenBagMessage.roomId.")
   
   def _maxRoomIdFunc(self,input) :
      self.maxRoomId = input.readByte()
      if(self.maxRoomId < 0) :
         raise RuntimeError("Forbidden value (" + self.maxRoomId + ") on element of MapComplementaryInformationsDataInHavenBagMessage.maxRoomId.")