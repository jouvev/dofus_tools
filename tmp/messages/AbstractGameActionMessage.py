class AbstractGameActionMessage:
   def __init__(self,input):
      self._actionIdFunc(input)
      self._sourceIdFunc(input)
   
   def _actionIdFunc(self,input) :
      self.actionId = input.readVarUhShort()
      if(self.actionId < 0) :
         raise RuntimeError("Forbidden value (" + self.actionId + ") on element of AbstractGameActionMessage.actionId.")
   
   def _sourceIdFunc(self,input) :
      self.sourceId = input.readDouble()
      if(self.sourceId < -9007199254740992 or self.sourceId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.sourceId + ") on element of AbstractGameActionMessage.sourceId.")