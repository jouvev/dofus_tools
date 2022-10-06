from tmp.types.IndexedEntityLook import IndexedEntityLook
from tmp.types.HumanOption import HumanOption

class HumanOptionFollowers(HumanOption):
   def __init__(self,input):
      self.followingCharactersLook = []
      _item1 = None
      super().__init__(input)
      _followingCharactersLookLen = input.readUnsignedShort()
      for _i1 in range(0,_followingCharactersLookLen):
         _item1 = IndexedEntityLook(input)
         self.followingCharactersLook.append(_item1)

   def resume(self):
      super().resume()
      for e in self.followingCharactersLook:
         e.resume()
