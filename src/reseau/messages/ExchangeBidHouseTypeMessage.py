class ExchangeBidHouseTypeMessage:
   def __init__(self,input):
      self._typeFunc(input)
      self._followFunc(input)
   
   def _typeFunc(self,input) :
      self.type = input.readVarUhInt()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of ExchangeBidHouseTypeMessage.type.")
   
   def _followFunc(self,input) :
      self.follow = input.readBoolean()

   def resume(self):
      print("type :",self.type)
      print("follow :",self.follow)
