class ExchangeBidHouseItemRemoveOkMessage:
   def __init__(self,input):
      self._sellerIdFunc(input)
   
   def _sellerIdFunc(self,input) :
      self.sellerId = input.readInt()