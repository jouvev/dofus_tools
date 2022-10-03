class ObjectGroundRemovedMessage:
   def __init__(self,input):
      self._cellFunc(input)
   
   def _cellFunc(self,input) :
      self.cell = input.readVarUhShort()
      if(self.cell < 0 or self.cell > 559) :
         raise RuntimeError("Forbidden value (" + self.cell + ") on element of ObjectGroundRemovedMessage.cell.")