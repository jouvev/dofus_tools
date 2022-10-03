class ChangeThemeRequestMessage:
   def __init__(self,input):
      self._themeFunc(input)
   
   def _themeFunc(self,input) :
      self.theme = input.readByte()