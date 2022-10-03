class ShortcutBarSwapRequestMessage:
   def __init__(self,input):
      self._barTypeFunc(input)
      self._firstSlotFunc(input)
      self._secondSlotFunc(input)
   
   def _barTypeFunc(self,input) :
      self.barType = input.readByte()
      if(self.barType < 0) :
         raise RuntimeError("Forbidden value (" + self.barType + ") on element of ShortcutBarSwapRequestMessage.barType.")
   
   def _firstSlotFunc(self,input) :
      self.firstSlot = input.readByte()
      if(self.firstSlot < 0 or self.firstSlot > 99) :
         raise RuntimeError("Forbidden value (" + self.firstSlot + ") on element of ShortcutBarSwapRequestMessage.firstSlot.")
   
   def _secondSlotFunc(self,input) :
      self.secondSlot = input.readByte()
      if(self.secondSlot < 0 or self.secondSlot > 99) :
         raise RuntimeError("Forbidden value (" + self.secondSlot + ") on element of ShortcutBarSwapRequestMessage.secondSlot.")