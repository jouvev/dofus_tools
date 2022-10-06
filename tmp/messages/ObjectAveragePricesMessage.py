class ObjectAveragePricesMessage:
   def __init__(self,input):
      self.ids = []
      self.avgPrices = []
      _val1 = 0
      _val2 = None
      _idsLen = input.readUnsignedShort()
      for _i1 in range(0,_idsLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of ids.")
         self.ids.append(_val1)
      _avgPricesLen = input.readUnsignedShort()
      for _i2 in range(0,_avgPricesLen):
         _val2 = input.readVarUhLong()
         if(_val2 < 0 or _val2 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of avgPrices.")
         self.avgPrices.append(_val2)

   def resume(self):
      print("ids :",self.ids)
      print("avgPrices :",self.avgPrices)
