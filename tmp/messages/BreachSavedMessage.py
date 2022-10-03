class BreachSavedMessage:
   def __init__(self,input):
      self._savedFunc(input)
   
   def _savedFunc(self,input) :
      self.saved = input.readBoolean()