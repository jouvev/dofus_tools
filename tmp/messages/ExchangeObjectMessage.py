class ExchangeObjectMessage:
   def __init__(self,input):
      self._remoteFunc(input)
   
   def _remoteFunc(self,input) :
      self.remote = input.readBoolean()