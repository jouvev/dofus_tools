class HaapiValidationMessage:
   def __init__(self,input):
      self._actionFunc(input)
      self._codeFunc(input)
   
   def _actionFunc(self,input) :
      self.action = input.readByte()
      if(self.action < 0) :
         raise RuntimeError("Forbidden value (" + self.action + ") on element of HaapiValidationMessage.action.")
   
   def _codeFunc(self,input) :
      self.code = input.readByte()
      if(self.code < 0) :
         raise RuntimeError("Forbidden value (" + self.code + ") on element of HaapiValidationMessage.code.")