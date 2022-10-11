from src.reseau.types.PaddockItem import PaddockItem

class GameDataPaddockObjectAddMessage:
   def __init__(self,input):
      self.paddockItemDescription = PaddockItem(input)

   def resume(self):
      self.paddockItemDescription.resume()
