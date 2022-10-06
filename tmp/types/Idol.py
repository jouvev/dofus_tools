class Idol:
   def __init__(self,input):
      self._idFunc(input)
      self._xpBonusPercentFunc(input)
      self._dropBonusPercentFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhShort()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of Idol.id.")
   
   def _xpBonusPercentFunc(self,input) :
      self.xpBonusPercent = input.readVarUhShort()
      if(self.xpBonusPercent < 0) :
         raise RuntimeError("Forbidden value (" + str(self.xpBonusPercent) + ") on element of Idol.xpBonusPercent.")
   
   def _dropBonusPercentFunc(self,input) :
      self.dropBonusPercent = input.readVarUhShort()
      if(self.dropBonusPercent < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dropBonusPercent) + ") on element of Idol.dropBonusPercent.")

   def resume(self):
      print("id :",self.id)
      print("xpBonusPercent :",self.xpBonusPercent)
      print("dropBonusPercent :",self.dropBonusPercent)
