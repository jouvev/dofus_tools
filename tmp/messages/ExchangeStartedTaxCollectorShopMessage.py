from tmp.types.ObjectItem import ObjectItem

class ExchangeStartedTaxCollectorShopMessage:
   def __init__(self,input):
      self.objects = []
      _item1 = None
      _objectsLen = input.readUnsignedShort()
      for _i1 in range(0,_objectsLen):
         _item1 = ObjectItem(input)
         self.objects.append(_item1)
      self._kamasFunc(input)
   
   def _kamasFunc(self,input) :
      self.kamas = input.readVarUhLong()
      if(self.kamas < 0 or self.kamas > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of ExchangeStartedTaxCollectorShopMessage.kamas.")

   def resume(self):
      print("kamas :",self.kamas)
      for e in self.objects:
         e.resume()
