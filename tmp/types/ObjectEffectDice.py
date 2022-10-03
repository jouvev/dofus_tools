from tmp.types.ObjectEffect import ObjectEffect
class ObjectEffectDice(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._diceNumFunc(input)
      self._diceSideFunc(input)
      self._diceConstFunc(input)
   
   def _diceNumFunc(self,input) :
      self.diceNum = input.readVarUhInt()
      if(self.diceNum < 0) :
         raise RuntimeError("Forbidden value (" + self.diceNum + ") on element of ObjectEffectDice.diceNum.")
   
   def _diceSideFunc(self,input) :
      self.diceSide = input.readVarUhInt()
      if(self.diceSide < 0) :
         raise RuntimeError("Forbidden value (" + self.diceSide + ") on element of ObjectEffectDice.diceSide.")
   
   def _diceConstFunc(self,input) :
      self.diceConst = input.readVarUhInt()
      if(self.diceConst < 0) :
         raise RuntimeError("Forbidden value (" + self.diceConst + ") on element of ObjectEffectDice.diceConst.")