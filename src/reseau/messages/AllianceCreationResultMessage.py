class AllianceCreationResultMessage:
   def __init__(self,input):
      self._resultFunc(input)
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + str(self.result) + ") on element of AllianceCreationResultMessage.result.")

   def resume(self):
      print("result :",self.result)
