class HaapiShopApiKeyMessage:
   def __init__(self,input):
      self._tokenFunc(input)
   
   def _tokenFunc(self,input) :
      self.token = input.readUTF()

   def resume(self):
      print("token :",self.token)
