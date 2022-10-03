class ExchangeObjectTransfertListToInvMessage:
   def __init__(self,input):
      self.ids = []
      _val1 = 0
      _idsLen = input.readUnsignedShort()
      for _i1 in range(0,_idsLen):
         _val1 = input.readVarUhInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of ids.")
         self.ids.append(_val1)