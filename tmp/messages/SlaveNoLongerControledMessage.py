class SlaveNoLongerControledMessage:
   def __init__(self,input):
      self._masterIdFunc(input)
      self._slaveIdFunc(input)
   
   def _masterIdFunc(self,input) :
      self.masterId = input.readDouble()
      if(self.masterId < -9007199254740992 or self.masterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element of SlaveNoLongerControledMessage.masterId.")
   
   def _slaveIdFunc(self,input) :
      self.slaveId = input.readDouble()
      if(self.slaveId < -9007199254740992 or self.slaveId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.slaveId) + ") on element of SlaveNoLongerControledMessage.slaveId.")

   def resume(self):
      print("masterId :",self.masterId)
      print("slaveId :",self.slaveId)
