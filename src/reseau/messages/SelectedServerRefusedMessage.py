class SelectedServerRefusedMessage:
   def __init__(self,input):
      self._serverIdFunc(input)
      self._errorFunc(input)
      self._serverStatusFunc(input)
   
   def _serverIdFunc(self,input) :
      self.serverId = input.readVarUhShort()
      if(self.serverId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.serverId) + ") on element of SelectedServerRefusedMessage.serverId.")
   
   def _errorFunc(self,input) :
      self.error = input.readByte()
      if(self.error < 0) :
         raise RuntimeError("Forbidden value (" + str(self.error) + ") on element of SelectedServerRefusedMessage.error.")
   
   def _serverStatusFunc(self,input) :
      self.serverStatus = input.readByte()
      if(self.serverStatus < 0) :
         raise RuntimeError("Forbidden value (" + str(self.serverStatus) + ") on element of SelectedServerRefusedMessage.serverStatus.")

   def resume(self):
      print("serverId :",self.serverId)
      print("error :",self.error)
      print("serverStatus :",self.serverStatus)
