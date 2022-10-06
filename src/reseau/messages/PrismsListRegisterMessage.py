class PrismsListRegisterMessage:
   def __init__(self,input):
      self._listenFunc(input)
   
   def _listenFunc(self,input) :
      self.listen = input.readByte()
      if(self.listen < 0) :
         raise RuntimeError("Forbidden value (" + str(self.listen) + ") on element of PrismsListRegisterMessage.listen.")

   def resume(self):
      print("listen :",self.listen)
