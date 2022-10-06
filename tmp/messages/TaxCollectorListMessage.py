from tmp.messages.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage
from tmp.types.TaxCollectorFightersInformation import TaxCollectorFightersInformation

class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
   def __init__(self,input):
      self.fightersInformations = []
      _item2 = None
      super().__init__(input)
      self._nbcollectorMaxFunc(input)
      _fightersInformationsLen = input.readUnsignedShort()
      for _i2 in range(0,_fightersInformationsLen):
         _item2 = TaxCollectorFightersInformation(input)
         self.fightersInformations.append(_item2)
      self._infoTypeFunc(input)
   
   def _nbcollectorMaxFunc(self,input) :
      self.nbcollectorMax = input.readByte()
      if(self.nbcollectorMax < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nbcollectorMax) + ") on element of TaxCollectorListMessage.nbcollectorMax.")
   
   def _infoTypeFunc(self,input) :
      self.infoType = input.readByte()
      if(self.infoType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.infoType) + ") on element of TaxCollectorListMessage.infoType.")

   def resume(self):
      super().resume()
      print("nbcollectorMax :",self.nbcollectorMax)
      print("infoType :",self.infoType)
      for e in self.fightersInformations:
         e.resume()
