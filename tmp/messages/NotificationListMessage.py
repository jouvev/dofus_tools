class NotificationListMessage:
   def __init__(self,input):
      self.flags = []
      _val1 = 0
      _flagsLen = input.readUnsignedShort()
      for _i1 in range(0,_flagsLen):
         _val1 = input.readVarInt()
         self.flags.append(_val1)

   def resume(self):
      print("flags :",self.flags)
