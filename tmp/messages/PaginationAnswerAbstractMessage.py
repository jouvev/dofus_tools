class PaginationAnswerAbstractMessage:
   def __init__(self,input):
      self._offsetFunc(input)
      self._countFunc(input)
      self._totalFunc(input)
   
   def _offsetFunc(self,input) :
      self.offset = input.readDouble()
      if(self.offset < 0 or self.offset > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.offset + ") on element of PaginationAnswerAbstractMessage.offset.")
   
   def _countFunc(self,input) :
      self.count = input.readUnsignedInt()
      if(self.count < 0 or self.count > 4294967295) :
         raise RuntimeError("Forbidden value (" + self.count + ") on element of PaginationAnswerAbstractMessage.count.")
   
   def _totalFunc(self,input) :
      self.total = input.readUnsignedInt()
      if(self.total < 0 or self.total > 4294967295) :
         raise RuntimeError("Forbidden value (" + self.total + ") on element of PaginationAnswerAbstractMessage.total.")