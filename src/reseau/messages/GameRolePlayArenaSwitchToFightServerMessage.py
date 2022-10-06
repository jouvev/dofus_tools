class GameRolePlayArenaSwitchToFightServerMessage:
   def __init__(self,input):
      self.ports = []
      self.ticket = []
      _val2 = 0
      _val3 = 0
      self._addressFunc(input)
      _portsLen = input.readUnsignedShort()
      for _i2 in range(0,_portsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of ports.")
         self.ports.append(_val2)
      _ticketLen = input.readVarInt()
      for _i3 in range(0,_ticketLen):
         _val3 = input.readByte()
         self.ticket.append(_val3)
   
   def _addressFunc(self,input) :
      self.address = input.readUTF()

   def resume(self):
      print("address :",self.address)
      print("ports :",self.ports)
      print("ticket :",self.ticket)
