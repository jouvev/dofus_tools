from tmp.types.ServerSessionConstant import ServerSessionConstant

class ServerSessionConstantLong(ServerSessionConstant):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readDouble()
      if(self.value < -9007199254740992 or self.value > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.value) + ") on element of ServerSessionConstantLong.value.")

   def resume(self):
      super().resume()
      print("value :",self.value)
