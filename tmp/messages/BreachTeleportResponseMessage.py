class BreachTeleportResponseMessage:
   def __init__(self,input):
      self._teleportedFunc(input)
   
   def _teleportedFunc(self,input) :
      self.teleported = input.readBoolean()