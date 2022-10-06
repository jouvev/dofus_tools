class ShortcutBarRemovedMessage:
   def __init__(self,input):
      self._barTypeFunc(input)
      self._slotFunc(input)
   
   def _barTypeFunc(self,input) :
      self.barType = input.readByte()
      if(self.barType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.barType) + ") on element of ShortcutBarRemovedMessage.barType.")
   
   def _slotFunc(self,input) :
      self.slot = input.readByte()
      if(self.slot < 0 or self.slot > 99) :
         raise RuntimeError("Forbidden value (" + str(self.slot) + ") on element of ShortcutBarRemovedMessage.slot.")

   def resume(self):
      print("barType :",self.barType)
      print("slot :",self.slot)
