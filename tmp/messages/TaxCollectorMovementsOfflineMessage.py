from tmp.types.TaxCollectorMovement import TaxCollectorMovement
class TaxCollectorMovementsOfflineMessage:
   def __init__(self,input):
      self.movements = []
      _item1 = None
      _movementsLen = input.readUnsignedShort()
      for _i1 in range(0,_movementsLen):
         _item1 = TaxCollectorMovement(input)
         self.movements.append(_item1)