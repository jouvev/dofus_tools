class PauseDialogMessage:
   def __init__(self,input):
      self._dialogTypeFunc(input)
   
   def _dialogTypeFunc(self,input) :
      self.dialogType = input.readByte()
      if(self.dialogType < 0) :
         raise RuntimeError("Forbidden value (" + self.dialogType + ") on element of PauseDialogMessage.dialogType.")