class HelloConnectMessage:
   def __init__(self,input):
      self.key = []
      _val2 = 0
      self._saltFunc(input)
      _keyLen = input.readVarInt()
      for _i2 in range(0,_keyLen):
         _val2 = input.readByte()
         self.key.append(_val2)
   
   def _saltFunc(self,input) :
      self.salt = input.readUTF()

   def resume(self):
      print("salt :",self.salt)
      print("key :",self.key)
