class InvalidPresetsMessage:
   def __init__(self,input):
      self.presetIds = []
      _val1 = 0
      _presetIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_presetIdsLen):
         _val1 = input.readShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of presetIds.")
         self.presetIds.append(_val1)