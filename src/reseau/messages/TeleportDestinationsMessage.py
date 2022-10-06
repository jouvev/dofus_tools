from src.reseau.types.TeleportDestination import TeleportDestination

class TeleportDestinationsMessage:
   def __init__(self,input):
      self.destinations = []
      _item2 = None
      self._typeFunc(input)
      _destinationsLen = input.readUnsignedShort()
      for _i2 in range(0,_destinationsLen):
         _item2 = TeleportDestination(input)
         self.destinations.append(_item2)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of TeleportDestinationsMessage.type.")

   def resume(self):
      print("type :",self.type)
      for e in self.destinations:
         e.resume()
