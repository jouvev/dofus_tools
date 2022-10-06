from tmp.messages.ExchangeCraftResultWithObjectDescMessage import ExchangeCraftResultWithObjectDescMessage

class ExchangeCraftResultMagicWithObjectDescMessage(ExchangeCraftResultWithObjectDescMessage):
   def __init__(self,input):
      super().__init__(input)
      self._magicPoolStatusFunc(input)
   
   def _magicPoolStatusFunc(self,input) :
      self.magicPoolStatus = input.readByte()

   def resume(self):
      super().resume()
      print("magicPoolStatus :",self.magicPoolStatus)
