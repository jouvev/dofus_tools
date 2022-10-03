class BreachReward:
   def __init__(self,input):
      self.buyLocks = []
      _val2 = 0
      self._idFunc(input)
      _buyLocksLen = input.readUnsignedShort()
      for _i2 in range(0,_buyLocksLen):
         _val2 = input.readByte()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of buyLocks.")
         self.buyLocks.append(_val2)
      self._buyCriterionFunc(input)
      self._remainingQtyFunc(input)
      self._priceFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of BreachReward.id.")
   
   def _buyCriterionFunc(self,input) :
      self.buyCriterion = input.readUTF()
   
   def _remainingQtyFunc(self,input) :
      self.remainingQty = input.readVarInt()
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhInt()
      if(self.price < 0) :
         raise RuntimeError("Forbidden value (" + self.price + ") on element of BreachReward.price.")