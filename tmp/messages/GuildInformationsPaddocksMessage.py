from tmp.types.PaddockContentInformations import PaddockContentInformations

class GuildInformationsPaddocksMessage:
   def __init__(self,input):
      self.paddocksInformations = []
      _item2 = None
      self._nbPaddockMaxFunc(input)
      _paddocksInformationsLen = input.readUnsignedShort()
      for _i2 in range(0,_paddocksInformationsLen):
         _item2 = PaddockContentInformations(input)
         self.paddocksInformations.append(_item2)
   
   def _nbPaddockMaxFunc(self,input) :
      self.nbPaddockMax = input.readByte()
      if(self.nbPaddockMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbPaddockMax) + ") on element of GuildInformationsPaddocksMessage.nbPaddockMax.")

   def resume(self):
      print("nbPaddockMax :",self.nbPaddockMax)
      for e in self.paddocksInformations:
         e.resume()
