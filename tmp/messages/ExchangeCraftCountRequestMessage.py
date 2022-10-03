class ExchangeCraftCountRequestMessage:
   def __init__(self,input):
      self._countFunc(input)
   
   def _countFunc(self,input) :
      self.count = input.readVarInt()