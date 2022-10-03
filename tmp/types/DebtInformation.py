class DebtInformation:
   def __init__(self,input):
      self._idFunc(input)
      self._timestampFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < 0 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of DebtInformation.id.")
   
   def _timestampFunc(self,input) :
      self.timestamp = input.readDouble()
      if(self.timestamp < 0 or self.timestamp > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.timestamp + ") on element of DebtInformation.timestamp.")