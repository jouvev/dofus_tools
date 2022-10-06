from tmp.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyPledgeLoyaltyRequestMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._loyalFunc(input)
   
   def _loyalFunc(self,input) :
      self.loyal = input.readBoolean()

   def resume(self):
      super().resume()
      print("loyal :",self.loyal)
