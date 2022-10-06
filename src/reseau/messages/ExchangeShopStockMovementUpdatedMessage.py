from src.reseau.types.ObjectItemToSell import ObjectItemToSell

class ExchangeShopStockMovementUpdatedMessage:
   def __init__(self,input):
      self.objectInfo = ObjectItemToSell(input)

   def resume(self):
      self.objectInfo.resum()
