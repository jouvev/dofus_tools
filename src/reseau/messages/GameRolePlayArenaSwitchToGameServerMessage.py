class GameRolePlayArenaSwitchToGameServerMessage:
   def __init__(self,input):
      self._validTokenFunc(input)
      self._tokenFunc(input)
      self._homeServerIdFunc(input)
   
   def _validTokenFunc(self,input) :
      self.validToken = input.readBoolean()
   
   def _tokenFunc(self,input) :
      self.token = input.readUTF()
   
   def _homeServerIdFunc(self,input) :
      self.homeServerId = input.readShort()

   def resume(self):
      print("validToken :",self.validToken)
      print("token :",self.token)
      print("homeServerId :",self.homeServerId)
