from src.reseau.messages.PresetUseResultMessage import PresetUseResultMessage

class PresetUseResultWithMissingIdsMessage(PresetUseResultMessage):
   def __init__(self,input):
      self.missingIds = []
      _val1 = 0
      super().__init__(input)
      _missingIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_missingIdsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of missingIds.")
         self.missingIds.append(_val1)

   def resume(self):
      super().resume()
      print("missingIds :",self.missingIds)
