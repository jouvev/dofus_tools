class GameFightTurnFinishMessage:
   def __init__(self,input):
      self._isAfkFunc(input)
   
   def _isAfkFunc(self,input) :
      self.isAfk = input.readBoolean()