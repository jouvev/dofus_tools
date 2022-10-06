class HavenBagPermissionsUpdateMessage:
   def __init__(self,input):
      self._permissionsFunc(input)
   
   def _permissionsFunc(self,input) :
      self.permissions = input.readInt()
      if(self.permissions < 0) :
         raise RuntimeError("Forbidden value (" + str(self.permissions) + ") on element of HavenBagPermissionsUpdateMessage.permissions.")

   def resume(self):
      print("permissions :",self.permissions)
