class OrnamentGainedMessage:
   def __init__(self,input):
      self._ornamentIdFunc(input)
   
   def _ornamentIdFunc(self,input) :
      self.ornamentId = input.readShort()
      if(self.ornamentId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.ornamentId) + ") on element of OrnamentGainedMessage.ornamentId.")

   def resume(self):
      print("ornamentId :",self.ornamentId)
