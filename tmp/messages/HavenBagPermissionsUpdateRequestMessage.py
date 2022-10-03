class HavenBagPermissionsUpdateRequestMessage:
   def __init__(self,input):
      self._permissionsFunc(input)
   
   def _permissionsFunc(self,input) :
      self.permissions = input.readInt()
      if(self.permissions < 0) :
         raise RuntimeError("Forbidden value (" + self.permissions + ") on element of HavenBagPermissionsUpdateRequestMessage.permissions.")