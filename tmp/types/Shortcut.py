class Shortcut:
   def __init__(self,input):
      self._slotFunc(input)
   
   def _slotFunc(self,input) :
      self.slot = input.readByte()
      if(self.slot < 0 or self.slot > 99) :
         raise RuntimeError("Forbidden value (" + self.slot + ") on element of Shortcut.slot.")