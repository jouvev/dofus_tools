class FinishMoveSetRequestMessage:
   def __init__(self,input):
      self._finishMoveIdFunc(input)
      self._finishMoveStateFunc(input)
   
   def _finishMoveIdFunc(self,input) :
      self.finishMoveId = input.readInt()
      if(self.finishMoveId < 0) :
         raise RuntimeError("Forbidden value (" + self.finishMoveId + ") on element of FinishMoveSetRequestMessage.finishMoveId.")
   
   def _finishMoveStateFunc(self,input) :
      self.finishMoveState = input.readBoolean()