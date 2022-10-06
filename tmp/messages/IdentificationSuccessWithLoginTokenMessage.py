from tmp.messages.IdentificationSuccessMessage import IdentificationSuccessMessage

class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
   def __init__(self,input):
      super().__init__(input)
      self._loginTokenFunc(input)
   
   def _loginTokenFunc(self,input) :
      self.loginToken = input.readUTF()

   def resume(self):
      super().resume()
      print("loginToken :",self.loginToken)
