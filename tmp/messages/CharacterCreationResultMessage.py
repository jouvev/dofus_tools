class CharacterCreationResultMessage:
   def __init__(self,input):
      self._resultFunc(input)
      self._reasonFunc(input)
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + str(self.result) + ") on element of CharacterCreationResultMessage.result.")
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()
      if(self.reason < 0) :
         raise RuntimeError("Forbidden value (" + str(self.reason) + ") on element of CharacterCreationResultMessage.reason.")

   def resume(self):
      print("result :",self.result)
      print("reason :",self.reason)
