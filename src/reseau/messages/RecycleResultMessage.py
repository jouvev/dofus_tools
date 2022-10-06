class RecycleResultMessage:
   def __init__(self,input):
      self._nuggetsForPrismFunc(input)
      self._nuggetsForPlayerFunc(input)
   
   def _nuggetsForPrismFunc(self,input) :
      self.nuggetsForPrism = input.readVarUhInt()
      if(self.nuggetsForPrism < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nuggetsForPrism) + ") on element of RecycleResultMessage.nuggetsForPrism.")
   
   def _nuggetsForPlayerFunc(self,input) :
      self.nuggetsForPlayer = input.readVarUhInt()
      if(self.nuggetsForPlayer < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nuggetsForPlayer) + ") on element of RecycleResultMessage.nuggetsForPlayer.")

   def resume(self):
      print("nuggetsForPrism :",self.nuggetsForPrism)
      print("nuggetsForPlayer :",self.nuggetsForPlayer)
