import tmp.TypesFactory as pf

class ShortcutBarContentMessage:
   def __init__(self,input):
      self.shortcuts = []
      _id2 = 0
      _item2 = None
      self._barTypeFunc(input)
      _shortcutsLen = input.readUnsignedShort()
      for _i2 in range(0,_shortcutsLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.shortcuts.append(_item2)
   
   def _barTypeFunc(self,input) :
      self.barType = input.readByte()
      if(self.barType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.barType) + ") on element of ShortcutBarContentMessage.barType.")

   def resume(self):
      print("barType :",self.barType)
      for e in self.shortcuts:
         e.resume()
