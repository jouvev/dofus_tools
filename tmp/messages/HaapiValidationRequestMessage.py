class HaapiValidationRequestMessage:
   def __init__(self,input):
      self._transactionFunc(input)
   
   def _transactionFunc(self,input) :
      self.transaction = input.readUTF()

   def resume(self):
      print("transaction :",self.transaction)
