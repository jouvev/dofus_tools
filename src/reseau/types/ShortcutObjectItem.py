from src.reseau.types.ShortcutObject import ShortcutObject

class ShortcutObjectItem(ShortcutObject):
   def __init__(self,input):
      super().__init__(input)
      self._itemUIDFunc(input)
      self._itemGIDFunc(input)
   
   def _itemUIDFunc(self,input) :
      self.itemUID = input.readInt()
   
   def _itemGIDFunc(self,input) :
      self.itemGID = input.readInt()

   def resume(self):
      super().resume()
      print("itemUID :",self.itemUID)
      print("itemGID :",self.itemGID)
