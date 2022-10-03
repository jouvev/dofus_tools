from tmp.types.ItemForPreset import ItemForPreset
from tmp.types.EntityLook import EntityLook
from tmp.types.Preset import Preset
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