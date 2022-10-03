from tmp.types.ItemDurability import ItemDurability
from tmp.types.ObjectItemInRolePlay import ObjectItemInRolePlay
class PaddockItem(ObjectItemInRolePlay):
   def __init__(self,input):
      super().__init__(input)
      self.durability = ItemDurability(input)