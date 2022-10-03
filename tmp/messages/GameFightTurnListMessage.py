class GameFightTurnListMessage:
   def __init__(self,input):
      self.ids = []
      self.deadsIds = []
      _val1 = None
      _val2 = None
      _idsLen = input.readUnsignedShort()
      for _i1 in range(0,_idsLen):
         _val1 = input.readDouble()
         if(_val1 < -9007199254740992 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of ids.")
         self.ids.append(_val1)
      _deadsIdsLen = input.readUnsignedShort()
      for _i2 in range(0,_deadsIdsLen):
         _val2 = input.readDouble()
         if(_val2 < -9007199254740992 or _val2 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of deadsIds.")
         self.deadsIds.append(_val2)