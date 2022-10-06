class ItemDurability:
   def __init__(self,input):
      self._durabilityFunc(input)
      self._durabilityMaxFunc(input)
   
   def _durabilityFunc(self,input) :
      self.durability = input.readShort()
   
   def _durabilityMaxFunc(self,input) :
      self.durabilityMax = input.readShort()

   def resume(self):
      print("durability :",self.durability)
      print("durabilityMax :",self.durabilityMax)
