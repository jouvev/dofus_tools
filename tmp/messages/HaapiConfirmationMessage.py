class HaapiConfirmationMessage:
   def __init__(self,input):
      self._kamasFunc(input)
      self._amountFunc(input)
      self._rateFunc(input)
      self._actionFunc(input)
      self._transactionFunc(input)
   
   def _kamasFunc(self,input) :
      self.kamas = input.readVarUhLong()
      if(self.kamas < 0 or self.kamas > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of HaapiConfirmationMessage.kamas.")
   
   def _amountFunc(self,input) :
      self.amount = input.readVarUhLong()
      if(self.amount < 0 or self.amount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.amount) + ") on element of HaapiConfirmationMessage.amount.")
   
   def _rateFunc(self,input) :
      self.rate = input.readVarUhShort()
      if(self.rate < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rate) + ") on element of HaapiConfirmationMessage.rate.")
   
   def _actionFunc(self,input) :
      self.action = input.readByte()
      if(self.action < 0) :
         raise RuntimeError("Forbidden value (" + str(self.action) + ") on element of HaapiConfirmationMessage.action.")
   
   def _transactionFunc(self,input) :
      self.transaction = input.readUTF()

   def resume(self):
      print("kamas :",self.kamas)
      print("amount :",self.amount)
      print("rate :",self.rate)
      print("action :",self.action)
      print("transaction :",self.transaction)
