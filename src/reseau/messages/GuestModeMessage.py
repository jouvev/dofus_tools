class GuestModeMessage:
   def __init__(self,input):
      self._activeFunc(input)
   
   def _activeFunc(self,input) :
      self.active = input.readBoolean()

   def resume(self):
      print("active :",self.active)
