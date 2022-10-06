class EnterHavenBagRequestMessage:
   def __init__(self,input):
      self._havenBagOwnerFunc(input)
   
   def _havenBagOwnerFunc(self,input) :
      self.havenBagOwner = input.readVarUhLong()
      if(self.havenBagOwner < 0 or self.havenBagOwner > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.havenBagOwner) + ") on element of EnterHavenBagRequestMessage.havenBagOwner.")

   def resume(self):
      print("havenBagOwner :",self.havenBagOwner)
