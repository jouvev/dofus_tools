class CheckIntegrityMessage:
   def __init__(self,input):
      self.data = []
      _val1 = 0
      _dataLen = input.readVarInt()
      for _i1 in range(0,_dataLen):
         _val1 = input.readByte()
         self.data.append(_val1)

   def resume(self):
      print("data :",self.data)
