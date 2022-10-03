class SellerBuyerDescriptor:
   def __init__(self,input):
      self.quantities = []
      self.types = []
      _val1 = 0
      _val2 = 0
      _quantitiesLen = input.readUnsignedShort()
      for _i1 in range(0,_quantitiesLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of quantities.")
         self.quantities.append(_val1)
      _typesLen = input.readUnsignedShort()
      for _i2 in range(0,_typesLen):
         _val2 = input.readVarUhInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of types.")
         self.types.append(_val2)
      self._taxPercentageFunc(input)
      self._taxModificationPercentageFunc(input)
      self._maxItemLevelFunc(input)
      self._maxItemPerAccountFunc(input)
      self._npcContextualIdFunc(input)
      self._unsoldDelayFunc(input)
   
   def _taxPercentageFunc(self,input) :
      self.taxPercentage = input.readFloat()
   
   def _taxModificationPercentageFunc(self,input) :
      self.taxModificationPercentage = input.readFloat()
   
   def _maxItemLevelFunc(self,input) :
      self.maxItemLevel = input.readUnsignedByte()
      if(self.maxItemLevel < 0 or self.maxItemLevel > 255) :
         raise RuntimeError("Forbidden value (" + self.maxItemLevel + ") on element of SellerBuyerDescriptor.maxItemLevel.")
   
   def _maxItemPerAccountFunc(self,input) :
      self.maxItemPerAccount = input.readVarUhInt()
      if(self.maxItemPerAccount < 0) :
         raise RuntimeError("Forbidden value (" + self.maxItemPerAccount + ") on element of SellerBuyerDescriptor.maxItemPerAccount.")
   
   def _npcContextualIdFunc(self,input) :
      self.npcContextualId = input.readInt()
   
   def _unsoldDelayFunc(self,input) :
      self.unsoldDelay = input.readVarUhShort()
      if(self.unsoldDelay < 0) :
         raise RuntimeError("Forbidden value (" + self.unsoldDelay + ") on element of SellerBuyerDescriptor.unsoldDelay.")