class Preset:
   def __init__(self,input):
      self._idFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readShort()