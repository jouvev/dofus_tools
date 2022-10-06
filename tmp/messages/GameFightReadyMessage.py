class GameFightReadyMessage:
   def __init__(self,input):
      self._isReadyFunc(input)
   
   def _isReadyFunc(self,input) :
      self.isReady = input.readBoolean()

   def resume(self):
      print("isReady :",self.isReady)
