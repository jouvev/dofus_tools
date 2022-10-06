class GameFightPauseMessage:
   def __init__(self,input):
      self._isPausedFunc(input)
   
   def _isPausedFunc(self,input) :
      self.isPaused = input.readBoolean()

   def resume(self):
      print("isPaused :",self.isPaused)
