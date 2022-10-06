class LockableShowCodeDialogMessage:
   def __init__(self,input):
      self._changeOrUseFunc(input)
      self._codeSizeFunc(input)
   
   def _changeOrUseFunc(self,input) :
      self.changeOrUse = input.readBoolean()
   
   def _codeSizeFunc(self,input) :
      self.codeSize = input.readByte()
      if(self.codeSize < 0) :
         raise RuntimeError("Forbidden value (" + str(self.codeSize) + ") on element of LockableShowCodeDialogMessage.codeSize.")

   def resume(self):
      print("changeOrUse :",self.changeOrUse)
      print("codeSize :",self.codeSize)
