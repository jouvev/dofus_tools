class ExchangeRequestedMessage:
   def __init__(self,input):
      self._exchangeTypeFunc(input)
   
   def _exchangeTypeFunc(self,input) :
      self.exchangeType = input.readByte()

   def resume(self):
      print("exchangeType :",self.exchangeType)
