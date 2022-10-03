class FightLootObject:
   def __init__(self,input):
      self._objectIdFunc(input)
      self._quantityFunc(input)
      self._priorityHintFunc(input)
   
   def _objectIdFunc(self,input) :
      self.objectId = input.readInt()
   
   def _quantityFunc(self,input) :
      self.quantity = input.readInt()
   
   def _priorityHintFunc(self,input) :
      self.priorityHint = input.readInt()