class ReloginTokenStatusMessage:
   def __init__(self,input):
      self._validTokenFunc(input)
      self._tokenFunc(input)
   
   def _validTokenFunc(self,input) :
      self.validToken = input.readBoolean()
   
   def _tokenFunc(self,input) :
      self.token = input.readUTF()

   def resume(self):
      print("validToken :",self.validToken)
      print("token :",self.token)
