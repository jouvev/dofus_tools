class ObjectGroundRemovedMessage:
   def __init__(self,input):
      self._cellFunc(input)
   
   def _cellFunc(self,input) :
      self.cell = input.readVarUhShort()
      if(self.cell < 0 or self.cell > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cell) + ") on element of ObjectGroundRemovedMessage.cell.")

   def resume(self):
      print("cell :",self.cell)
