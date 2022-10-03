class MigratedServerListMessage:
   def __init__(self,input):
      self.migratedServerIds = []
      _val1 = 0
      _migratedServerIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_migratedServerIdsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of migratedServerIds.")
         self.migratedServerIds.append(_val1)