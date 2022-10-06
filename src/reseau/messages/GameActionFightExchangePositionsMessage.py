from src.reseau.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightExchangePositionsMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._casterCellIdFunc(input)
      self._targetCellIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightExchangePositionsMessage.targetId.")
   
   def _casterCellIdFunc(self,input) :
      self.casterCellId = input.readShort()
      if(self.casterCellId < -1 or self.casterCellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.casterCellId) + ") on element of GameActionFightExchangePositionsMessage.casterCellId.")
   
   def _targetCellIdFunc(self,input) :
      self.targetCellId = input.readShort()
      if(self.targetCellId < -1 or self.targetCellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.targetCellId) + ") on element of GameActionFightExchangePositionsMessage.targetCellId.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("casterCellId :",self.casterCellId)
      print("targetCellId :",self.targetCellId)
