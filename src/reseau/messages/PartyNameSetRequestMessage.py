from src.reseau.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyNameSetRequestMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._partyNameFunc(input)
   
   def _partyNameFunc(self,input) :
      self.partyName = input.readUTF()

   def resume(self):
      super().resume()
      print("partyName :",self.partyName)
