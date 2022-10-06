from tmp.types.ObjectEffect import ObjectEffect

class ObjectEffectDuration(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._daysFunc(input)
      self._hoursFunc(input)
      self._minutesFunc(input)
   
   def _daysFunc(self,input) :
      self.days = input.readVarUhShort()
      if(self.days < 0) :
         raise RuntimeError("Forbidden value (" + str(self.days) + ") on element of ObjectEffectDuration.days.")
   
   def _hoursFunc(self,input) :
      self.hours = input.readByte()
      if(self.hours < 0) :
         raise RuntimeError("Forbidden value (" + str(self.hours) + ") on element of ObjectEffectDuration.hours.")
   
   def _minutesFunc(self,input) :
      self.minutes = input.readByte()
      if(self.minutes < 0) :
         raise RuntimeError("Forbidden value (" + str(self.minutes) + ") on element of ObjectEffectDuration.minutes.")

   def resume(self):
      super().resume()
      print("days :",self.days)
      print("hours :",self.hours)
      print("minutes :",self.minutes)
