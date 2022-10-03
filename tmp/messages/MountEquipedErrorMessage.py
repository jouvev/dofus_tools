class MountEquipedErrorMessage:
   def __init__(self,input):
      self._errorTypeFunc(input)
   
   def _errorTypeFunc(self,input) :
      self.errorType = input.readByte()
      if(self.errorType < 0) :
         raise RuntimeError("Forbidden value (" + self.errorType + ") on element of MountEquipedErrorMessage.errorType.")