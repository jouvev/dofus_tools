class AreaFightModificatorUpdateMessage:
   def __init__(self,input):
      self._spellPairIdFunc(input)
   
   def _spellPairIdFunc(self,input) :
      self.spellPairId = input.readInt()

   def resume(self):
      print("spellPairId :",self.spellPairId)
