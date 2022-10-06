class PlayerStatus:
   def __init__(self,input):
      self._statusIdFunc(input)
   
   def _statusIdFunc(self,input) :
      self.statusId = input.readByte()
      if(self.statusId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.statusId) + ") on element of PlayerStatus.statusId.")

   def resume(self):
      print("statusId :",self.statusId)
