class MonsterBoosts:
   def __init__(self,input):
      self._idFunc(input)
      self._xpBoostFunc(input)
      self._dropBoostFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of MonsterBoosts.id.")
   
   def _xpBoostFunc(self,input) :
      self.xpBoost = input.readVarUhShort()
      if(self.xpBoost < 0) :
         raise RuntimeError("Forbidden value (" + str(self.xpBoost) + ") on element of MonsterBoosts.xpBoost.")
   
   def _dropBoostFunc(self,input) :
      self.dropBoost = input.readVarUhShort()
      if(self.dropBoost < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dropBoost) + ") on element of MonsterBoosts.dropBoost.")

   def resume(self):
      print("id :",self.id)
      print("xpBoost :",self.xpBoost)
      print("dropBoost :",self.dropBoost)
