from tmp.messages.ObjectUseMessage import ObjectUseMessage
class ObjectUseOnCellMessage(ObjectUseMessage):
   def __init__(self,input):
      super().__init__(input)
      self._cellsFunc(input)
   
   def _cellsFunc(self,input) :
      self.cells = input.readVarUhShort()
      if(self.cells < 0 or self.cells > 559) :
         raise RuntimeError("Forbidden value (" + self.cells + ") on element of ObjectUseOnCellMessage.cells.")