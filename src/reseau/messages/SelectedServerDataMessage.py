class SelectedServerDataMessage:
   def __init__(self,input):
      self.ports = []
      self.ticket = []
      _val3 = 0
      _val5 = 0
      self._serverIdFunc(input)
      self._addressFunc(input)
      _portsLen = input.readUnsignedShort()
      for _i3 in range(0,_portsLen):
         _val3 = input.readVarUhShort()
         if(_val3 < 0) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of ports.")
         self.ports.append(_val3)
      self._canCreateNewCharacterFunc(input)
      _ticketLen = input.readVarInt()
      for _i5 in range(0,_ticketLen):
         _val5 = input.readByte()
         self.ticket.append(_val5)
   
   def _serverIdFunc(self,input) :
      self.serverId = input.readVarUhShort()
      if(self.serverId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.serverId) + ") on element of SelectedServerDataMessage.serverId.")
   
   def _addressFunc(self,input) :
      self.address = input.readUTF()
   
   def _canCreateNewCharacterFunc(self,input) :
      self.canCreateNewCharacter = input.readBoolean()

   def resume(self):
      print("serverId :",self.serverId)
      print("address :",self.address)
      print("canCreateNewCharacter :",self.canCreateNewCharacter)
      print("ports :",self.ports)
      print("ticket :",self.ticket)
