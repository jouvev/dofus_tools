class MountHarnessColorsUpdateRequestMessage:
   def __init__(self,input):
      self._useHarnessColorsFunc(input)
   
   def _useHarnessColorsFunc(self,input) :
      self.useHarnessColors = input.readBoolean()