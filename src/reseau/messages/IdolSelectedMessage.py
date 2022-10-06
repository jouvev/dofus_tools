class IdolSelectedMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._idolIdFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.activate = bool(bin(_box0)[2:].zfill(8)[0])
      self.party = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _idolIdFunc(self,input) :
      self.idolId = input.readVarUhShort()
      if(self.idolId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.idolId) + ") on element of IdolSelectedMessage.idolId.")

   def resume(self):
      print("idolId :",self.idolId)
