from tmp.messages.ClientUIOpenedMessage import ClientUIOpenedMessage

class ClientUIOpenedByObjectMessage(ClientUIOpenedMessage):
   def __init__(self,input):
      super().__init__(input)
      self._uidFunc(input)
   
   def _uidFunc(self,input) :
      self.uid = input.readVarUhInt()
      if(self.uid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of ClientUIOpenedByObjectMessage.uid.")

   def resume(self):
      super().resume()
      print("uid :",self.uid)
