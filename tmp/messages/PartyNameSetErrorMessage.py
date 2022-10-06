from tmp.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyNameSetErrorMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._resultFunc(input)
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + str(self.result) + ") on element of PartyNameSetErrorMessage.result.")

   def resume(self):
      super().resume()
      print("result :",self.result)
