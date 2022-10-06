from src.reseau.messages.HaapiValidationMessage import HaapiValidationMessage

class HaapiBuyValidationMessage(HaapiValidationMessage):
   def __init__(self,input):
      super().__init__(input)
      self._amountFunc(input)
      self._emailFunc(input)
   
   def _amountFunc(self,input) :
      self.amount = input.readVarUhLong()
      if(self.amount < 0 or self.amount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.amount) + ") on element of HaapiBuyValidationMessage.amount.")
   
   def _emailFunc(self,input) :
      self.email = input.readUTF()

   def resume(self):
      super().resume()
      print("amount :",self.amount)
      print("email :",self.email)
