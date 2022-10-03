from tmp.types.ObjectEffect import ObjectEffect
class ObjectEffectDate(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._yearFunc(input)
      self._monthFunc(input)
      self._dayFunc(input)
      self._hourFunc(input)
      self._minuteFunc(input)
   
   def _yearFunc(self,input) :
      self.year = input.readVarUhShort()
      if(self.year < 0) :
         raise RuntimeError("Forbidden value (" + self.year + ") on element of ObjectEffectDate.year.")
   
   def _monthFunc(self,input) :
      self.month = input.readByte()
      if(self.month < 0) :
         raise RuntimeError("Forbidden value (" + self.month + ") on element of ObjectEffectDate.month.")
   
   def _dayFunc(self,input) :
      self.day = input.readByte()
      if(self.day < 0) :
         raise RuntimeError("Forbidden value (" + self.day + ") on element of ObjectEffectDate.day.")
   
   def _hourFunc(self,input) :
      self.hour = input.readByte()
      if(self.hour < 0) :
         raise RuntimeError("Forbidden value (" + self.hour + ") on element of ObjectEffectDate.hour.")
   
   def _minuteFunc(self,input) :
      self.minute = input.readByte()
      if(self.minute < 0) :
         raise RuntimeError("Forbidden value (" + self.minute + ") on element of ObjectEffectDate.minute.")