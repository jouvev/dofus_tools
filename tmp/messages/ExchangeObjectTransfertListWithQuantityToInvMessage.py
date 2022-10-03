class ExchangeObjectTransfertListWithQuantityToInvMessage:
   def __init__(self,input):
      self.ids = []
      self.qtys = []
      _val1 = 0
      _val2 = 0
      _idsLen = input.readUnsignedShort()
      for _i1 in range(0,_idsLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of ids.")
         self.ids.append(_val1)
      _qtysLen = input.readUnsignedShort()
      for _i2 in range(0,_qtysLen):
         _val2 = input.readVarUhInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of qtys.")
         self.qtys.append(_val2)