class ExchangeErrorMessage:
   def __init__(self,input):
      self._errorTypeFunc(input)
   
   def _errorTypeFunc(self,input) :
      self.errorType = input.readByte()