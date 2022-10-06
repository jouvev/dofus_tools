class ExchangeCraftCountRequestMessage:
   def __init__(self,input):
      self._countFunc(input)
   
   def _countFunc(self,input) :
      self.count = input.readVarInt()

   def resume(self):
      print("count :",self.count)
