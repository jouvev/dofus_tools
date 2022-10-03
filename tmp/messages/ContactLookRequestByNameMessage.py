from tmp.messages.ContactLookRequestMessage import ContactLookRequestMessage
class ContactLookRequestByNameMessage(ContactLookRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._playerNameFunc(input)
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()