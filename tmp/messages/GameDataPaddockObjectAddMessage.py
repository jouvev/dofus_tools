from tmp.types.PaddockItem import PaddockItem
class GameDataPaddockObjectAddMessage:
   def __init__(self,input):
      self.paddockItemDescription = PaddockItem(input)