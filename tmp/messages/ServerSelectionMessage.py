class ServerSelectionMessage:
   def __init__(self,input):
      self._serverIdFunc(input)
   
   def _serverIdFunc(self,input) :
      self.serverId = input.readVarUhShort()
      if(self.serverId < 0) :
         raise RuntimeError("Forbidden value (" + self.serverId + ") on element of ServerSelectionMessage.serverId.")