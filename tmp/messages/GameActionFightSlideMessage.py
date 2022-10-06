from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightSlideMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._startCellIdFunc(input)
      self._endCellIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightSlideMessage.targetId.")
   
   def _startCellIdFunc(self,input) :
      self.startCellId = input.readShort()
      if(self.startCellId < -1 or self.startCellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.startCellId) + ") on element of GameActionFightSlideMessage.startCellId.")
   
   def _endCellIdFunc(self,input) :
      self.endCellId = input.readShort()
      if(self.endCellId < -1 or self.endCellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.endCellId) + ") on element of GameActionFightSlideMessage.endCellId.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("startCellId :",self.startCellId)
      print("endCellId :",self.endCellId)
