from src.reseau.types.ItemDurability import ItemDurability
from src.reseau.types.ObjectItemInRolePlay import ObjectItemInRolePlay

class PaddockItem(ObjectItemInRolePlay):
   def __init__(self,input):
      super().__init__(input)
      self.durability = ItemDurability(input)

   def resume(self):
      super().resume()
      self.durability.resume()
