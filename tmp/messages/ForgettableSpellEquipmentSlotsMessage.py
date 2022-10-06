class ForgettableSpellEquipmentSlotsMessage:
   def __init__(self,input):
      self._quantityFunc(input)
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarShort()

   def resume(self):
      print("quantity :",self.quantity)
