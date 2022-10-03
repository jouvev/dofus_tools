class PopupWarningMessage:
   def __init__(self,input):
      self._lockDurationFunc(input)
      self._authorFunc(input)
      self._contentFunc(input)
   
   def _lockDurationFunc(self,input) :
      self.lockDuration = input.readUnsignedByte()
      if(self.lockDuration < 0 or self.lockDuration > 255) :
         raise RuntimeError("Forbidden value (" + self.lockDuration + ") on element of PopupWarningMessage.lockDuration.")
   
   def _authorFunc(self,input) :
      self.author = input.readUTF()
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()