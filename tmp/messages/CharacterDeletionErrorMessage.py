class CharacterDeletionErrorMessage:
   def __init__(self,input):
      self._reasonFunc(input)
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()
      if(self.reason < 0) :
         raise RuntimeError("Forbidden value (" + str(self.reason) + ") on element of CharacterDeletionErrorMessage.reason.")

   def resume(self):
      print("reason :",self.reason)
