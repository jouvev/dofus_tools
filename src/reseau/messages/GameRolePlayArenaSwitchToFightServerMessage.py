class GameRolePlayArenaSwitchToFightServerMessage:
   def __init__(self,input):
      self.ports = []
      _val2 = 0
      self._addressFunc(input)
      _portsLen = input.readUnsignedShort()
      for _i2 in range(0,_portsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of ports.")
         self.ports.append(_val2)
      self._tokenFunc(input)
   
   def _addressFunc(self,input) :
      self.address = input.readUTF()
   
   def _tokenFunc(self,input) :
      self.token = input.readUTF()

   def resume(self):
      print("address :",self.address)
      print("token :",self.token)
      print("ports :",self.ports)
