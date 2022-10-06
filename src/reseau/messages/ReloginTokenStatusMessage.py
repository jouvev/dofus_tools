class ReloginTokenStatusMessage:
   def __init__(self,input):
      self.ticket = []
      _val2 = 0
      self._validTokenFunc(input)
      _ticketLen = input.readVarInt()
      for _i2 in range(0,_ticketLen):
         _val2 = input.readByte()
         self.ticket.append(_val2)
   
   def _validTokenFunc(self,input) :
      self.validToken = input.readBoolean()

   def resume(self):
      print("validToken :",self.validToken)
      print("ticket :",self.ticket)
