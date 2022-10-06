class HouseKickRequestMessage:
   def __init__(self,input):
      self._idFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhLong()
      if(self.id < 0 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of HouseKickRequestMessage.id.")

   def resume(self):
      print("id :",self.id)
