class ClientKeyMessage:
   def __init__(self,input):
      self._keyFunc(input)
   
   def _keyFunc(self,input) :
      self.key = input.readUTF()

   def resume(self):
      print("key :",self.key)
