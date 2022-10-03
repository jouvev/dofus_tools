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