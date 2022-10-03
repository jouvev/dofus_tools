class HaapiValidationRequestMessage:
   def __init__(self,input):
      self._transactionFunc(input)
   
   def _transactionFunc(self,input) :
      self.transaction = input.readUTF()