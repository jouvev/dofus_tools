from tmp.types.AbstractFightDispellableEffect import AbstractFightDispellableEffect

class FightTriggeredEffect(AbstractFightDispellableEffect):
   def __init__(self,input):
      super().__init__(input)
      self._param1Func(input)
      self._param2Func(input)
      self._param3Func(input)
      self._delayFunc(input)
   
   def _param1Func(self,input) :
      self.param1 = input.readInt()
   
   def _param2Func(self,input) :
      self.param2 = input.readInt()
   
   def _param3Func(self,input) :
      self.param3 = input.readInt()
   
   def _delayFunc(self,input) :
      self.delay = input.readShort()

   def resume(self):
      super().resume()
      print("param1 :",self.param1)
      print("param2 :",self.param2)
      print("param3 :",self.param3)
      print("delay :",self.delay)
