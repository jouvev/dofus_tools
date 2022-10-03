class PrismFightJoinLeaveRequestMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._joinFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PrismFightJoinLeaveRequestMessage.subAreaId.")
   
   def _joinFunc(self,input) :
      self.join = input.readBoolean()