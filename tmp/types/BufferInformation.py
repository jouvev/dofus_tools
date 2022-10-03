class BufferInformation:
   def __init__(self,input):
      self._idFunc(input)
      self._amountFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhLong()
      if(self.id < 0 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of BufferInformation.id.")
   
   def _amountFunc(self,input) :
      self.amount = input.readVarUhLong()
      if(self.amount < 0 or self.amount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.amount + ") on element of BufferInformation.amount.")