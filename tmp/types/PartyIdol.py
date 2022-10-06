from tmp.types.Idol import Idol

class PartyIdol(Idol):
   def __init__(self,input):
      self.ownersIds = []
      _val1 = None
      super().__init__(input)
      _ownersIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_ownersIdsLen):
         _val1 = input.readVarUhLong()
         if(_val1 < 0 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of ownersIds.")
         self.ownersIds.append(_val1)

   def resume(self):
      super().resume()
      print("ownersIds :",self.ownersIds)
