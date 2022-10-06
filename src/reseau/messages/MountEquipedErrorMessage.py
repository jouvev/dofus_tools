class MountEquipedErrorMessage:
   def __init__(self,input):
      self._errorTypeFunc(input)
   
   def _errorTypeFunc(self,input) :
      self.errorType = input.readByte()
      if(self.errorType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.errorType) + ") on element of MountEquipedErrorMessage.errorType.")

   def resume(self):
      print("errorType :",self.errorType)
