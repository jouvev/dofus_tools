from tmp.types.SellerBuyerDescriptor import SellerBuyerDescriptor

class ExchangeStartedBidBuyerMessage:
   def __init__(self,input):
      self.buyerDescriptor = SellerBuyerDescriptor(input)

   def resume(self):
      self.buyerDescriptor.resum()
