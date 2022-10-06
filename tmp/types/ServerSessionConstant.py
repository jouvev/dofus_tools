class ServerSessionConstant:
   def __init__(self,input):
      self._idFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhShort()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of ServerSessionConstant.id.")

   def resume(self):
      print("id :",self.id)
