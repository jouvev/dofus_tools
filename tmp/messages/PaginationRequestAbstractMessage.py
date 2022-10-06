class PaginationRequestAbstractMessage:
   def __init__(self,input):
      self._offsetFunc(input)
      self._countFunc(input)
   
   def _offsetFunc(self,input) :
      self.offset = input.readDouble()
      if(self.offset < 0 or self.offset > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.offset) + ") on element of PaginationRequestAbstractMessage.offset.")
   
   def _countFunc(self,input) :
      self.count = input.readUnsignedInt()
      if(self.count < 0 or self.count > 4294967295) :
         raise RuntimeError("Forbidden value (" + str(self.count) + ") on element of PaginationRequestAbstractMessage.count.")

   def resume(self):
      print("offset :",self.offset)
      print("count :",self.count)
