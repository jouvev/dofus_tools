from tmp.messages.ObjectErrorMessage import ObjectErrorMessage
class SymbioticObjectErrorMessage(ObjectErrorMessage):
   def __init__(self,input):
      super().__init__(input)
      self._errorCodeFunc(input)
   
   def _errorCodeFunc(self,input) :
      self.errorCode = input.readByte()