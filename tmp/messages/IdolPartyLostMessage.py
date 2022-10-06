class IdolPartyLostMessage:
   def __init__(self,input):
      self._idolIdFunc(input)
   
   def _idolIdFunc(self,input) :
      self.idolId = input.readVarUhShort()
      if(self.idolId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.idolId) + ") on element of IdolPartyLostMessage.idolId.")

   def resume(self):
      print("idolId :",self.idolId)
