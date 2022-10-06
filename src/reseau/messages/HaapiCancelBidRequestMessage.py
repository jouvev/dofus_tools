class HaapiCancelBidRequestMessage:
   def __init__(self,input):
      self._idFunc(input)
      self._typeFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhLong()
      if(self.id < 0 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of HaapiCancelBidRequestMessage.id.")
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of HaapiCancelBidRequestMessage.type.")

   def resume(self):
      print("id :",self.id)
      print("type :",self.type)
