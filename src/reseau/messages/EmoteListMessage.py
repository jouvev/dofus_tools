class EmoteListMessage:
   def __init__(self,input):
      self.emoteIds = []
      _val1 = 0
      _emoteIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_emoteIdsLen):
         _val1 = input.readUnsignedShort()
         if(_val1 < 0 or _val1 > 65535) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of emoteIds.")
         self.emoteIds.append(_val1)

   def resume(self):
      print("emoteIds :",self.emoteIds)
