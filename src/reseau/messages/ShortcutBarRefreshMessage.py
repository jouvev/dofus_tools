import src.reseau.TypesFactory as pf

class ShortcutBarRefreshMessage:
   def __init__(self,input):
      self._barTypeFunc(input)
      _id2 = input.readUnsignedShort()
      self.shortcut = pf.TypesFactory.get_instance_id(_id2,input)
   
   def _barTypeFunc(self,input) :
      self.barType = input.readByte()
      if(self.barType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.barType) + ") on element of ShortcutBarRefreshMessage.barType.")

   def resume(self):
      print("barType :",self.barType)
