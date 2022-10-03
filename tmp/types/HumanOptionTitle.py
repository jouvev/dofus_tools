from tmp.types.HumanOption import HumanOption
class HumanOptionTitle(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self._titleIdFunc(input)
      self._titleParamFunc(input)
   
   def _titleIdFunc(self,input) :
      self.titleId = input.readVarUhShort()
      if(self.titleId < 0) :
         raise RuntimeError("Forbidden value (" + self.titleId + ") on element of HumanOptionTitle.titleId.")
   
   def _titleParamFunc(self,input) :
      self.titleParam = input.readUTF()