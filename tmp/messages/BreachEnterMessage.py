class BreachEnterMessage:
   def __init__(self,input):
      self._ownerFunc(input)
   
   def _ownerFunc(self,input) :
      self.owner = input.readVarUhLong()
      if(self.owner < 0 or self.owner > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.owner) + ") on element of BreachEnterMessage.owner.")

   def resume(self):
      print("owner :",self.owner)
