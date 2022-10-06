from tmp.types.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations

class GameEntitiesDispositionMessage:
   def __init__(self,input):
      self.dispositions = []
      _item1 = None
      _dispositionsLen = input.readUnsignedShort()
      for _i1 in range(0,_dispositionsLen):
         _item1 = IdentifiedEntityDispositionInformations(input)
         self.dispositions.append(_item1)

   def resume(self):
      for e in self.dispositions:
         e.resume()
