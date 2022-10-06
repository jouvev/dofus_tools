class TaxCollectorErrorMessage:
   def __init__(self,input):
      self._reasonFunc(input)
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()

   def resume(self):
      print("reason :",self.reason)
