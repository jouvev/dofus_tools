from src.reseau.types.ItemForPreset import ItemForPreset
from src.reseau.types.EntityLook import EntityLook
from src.reseau.types.Preset import Preset

class ItemsPreset(Preset):
   def __init__(self,input):
      self.items = []
      _item1 = None
      super().__init__(input)
      _itemsLen = input.readUnsignedShort()
      for _i1 in range(0,_itemsLen):
         _item1 = ItemForPreset(input)
         self.items.append(_item1)
      self._mountEquippedFunc(input)
      self.look = EntityLook(input)
   
   def _mountEquippedFunc(self,input) :
      self.mountEquipped = input.readBoolean()

   def resume(self):
      super().resume()
      print("mountEquipped :",self.mountEquipped)
      self.look.resum()
      for e in self.items:
         e.resume()
