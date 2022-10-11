from src.reseau.types.ObjectItemToSellInBid import ObjectItemToSellInBid

class ExchangeBidHouseItemAddOkMessage:
   def __init__(self,input):
      self.itemInfo = ObjectItemToSellInBid(input)

   def resume(self):
      self.itemInfo.resume()
