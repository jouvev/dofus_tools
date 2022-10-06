from tmp.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyRestrictedMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._restrictedFunc(input)
   
   def _restrictedFunc(self,input) :
      self.restricted = input.readBoolean()

   def resume(self):
      super().resume()
      print("restricted :",self.restricted)
