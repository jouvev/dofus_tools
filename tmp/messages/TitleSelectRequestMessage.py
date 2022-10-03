class TitleSelectRequestMessage:
   def __init__(self,input):
      self._titleIdFunc(input)
   
   def _titleIdFunc(self,input) :
      self.titleId = input.readVarUhShort()
      if(self.titleId < 0) :
         raise RuntimeError("Forbidden value (" + self.titleId + ") on element of TitleSelectRequestMessage.titleId.")