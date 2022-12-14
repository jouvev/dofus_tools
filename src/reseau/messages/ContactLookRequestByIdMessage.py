from src.reseau.messages.ContactLookRequestMessage import ContactLookRequestMessage

class ContactLookRequestByIdMessage(ContactLookRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._playerIdFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of ContactLookRequestByIdMessage.playerId.")

   def resume(self):
      super().resume()
      print("playerId :",self.playerId)
