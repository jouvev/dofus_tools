class LockableStateUpdateAbstractMessage:
   def __init__(self,input):
      self._lockedFunc(input)
   
   def _lockedFunc(self,input) :
      self.locked = input.readBoolean()

   def resume(self):
      print("locked :",self.locked)
