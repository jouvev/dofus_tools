from tmp.types.GoldItem import GoldItem
class GoldAddedMessage:
   def __init__(self,input):
      self.gold = GoldItem(input)