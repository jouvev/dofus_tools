from src.reseau.types.GoldItem import GoldItem

class GoldAddedMessage:
   def __init__(self,input):
      self.gold = GoldItem(input)

   def resume(self):
      self.gold.resume()
