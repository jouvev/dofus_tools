class ExchangeMountsStableRemoveMessage:
   def __init__(self,input):
      self.mountsId = []
      _val1 = 0
      _mountsIdLen = input.readUnsignedShort()
      for _i1 in range(0,_mountsIdLen):
         _val1 = input.readVarInt()
         self.mountsId.append(_val1)