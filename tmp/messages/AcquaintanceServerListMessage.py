class AcquaintanceServerListMessage:
   def __init__(self,input):
      self.servers = []
      _val1 = 0
      _serversLen = input.readUnsignedShort()
      for _i1 in range(0,_serversLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of servers.")
         self.servers.append(_val1)

   def resume(self):
      print("servers :",self.servers)
