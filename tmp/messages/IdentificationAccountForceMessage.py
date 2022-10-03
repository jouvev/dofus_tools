from tmp.messages.IdentificationMessage import IdentificationMessage
class IdentificationAccountForceMessage(IdentificationMessage):
   def __init__(self,input):
      super().__init__(input)
      self._forcerAccountLoginFunc(input)
   
   def _forcerAccountLoginFunc(self,input) :
      self.forcerAccountLogin = input.readUTF()