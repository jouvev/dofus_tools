from src.reseau.types.ServerSessionConstant import ServerSessionConstant

class ServerSessionConstantInteger(ServerSessionConstant):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readInt()

   def resume(self):
      super().resume()
      print("value :",self.value)
