class WarnOnPermaDeathStateMessage:
   def __init__(self,input):
      self._enableFunc(input)
   
   def _enableFunc(self,input) :
      self.enable = input.readBoolean()