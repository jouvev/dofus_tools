from tmp.messages.TeleportDestinationsMessage import TeleportDestinationsMessage
class ZaapDestinationsMessage(TeleportDestinationsMessage):
   def __init__(self,input):
      super().__init__(input)
      self._spawnMapIdFunc(input)
   
   def _spawnMapIdFunc(self,input) :
      self.spawnMapId = input.readDouble()
      if(self.spawnMapId < 0 or self.spawnMapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.spawnMapId + ") on element of ZaapDestinationsMessage.spawnMapId.")