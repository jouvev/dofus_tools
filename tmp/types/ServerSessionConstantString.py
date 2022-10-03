from tmp.types.ServerSessionConstant import ServerSessionConstant
class ServerSessionConstantString(ServerSessionConstant):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readUTF()