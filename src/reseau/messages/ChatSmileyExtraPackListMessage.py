class ChatSmileyExtraPackListMessage:
   def __init__(self,input):
      self.packIds = []
      _val1 = 0
      _packIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_packIdsLen):
         _val1 = input.readByte()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of packIds.")
         self.packIds.append(_val1)

   def resume(self):
      print("packIds :",self.packIds)
