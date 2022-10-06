from tmp.messages.ExchangeStartedMessage import ExchangeStartedMessage

class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
   def __init__(self,input):
      super().__init__(input)
      self._firstCharacterIdFunc(input)
      self._firstCharacterCurrentWeightFunc(input)
      self._firstCharacterMaxWeightFunc(input)
      self._secondCharacterIdFunc(input)
      self._secondCharacterCurrentWeightFunc(input)
      self._secondCharacterMaxWeightFunc(input)
   
   def _firstCharacterIdFunc(self,input) :
      self.firstCharacterId = input.readDouble()
      if(self.firstCharacterId < -9007199254740992 or self.firstCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.firstCharacterId) + ") on element of ExchangeStartedWithPodsMessage.firstCharacterId.")
   
   def _firstCharacterCurrentWeightFunc(self,input) :
      self.firstCharacterCurrentWeight = input.readVarUhInt()
      if(self.firstCharacterCurrentWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.firstCharacterCurrentWeight) + ") on element of ExchangeStartedWithPodsMessage.firstCharacterCurrentWeight.")
   
   def _firstCharacterMaxWeightFunc(self,input) :
      self.firstCharacterMaxWeight = input.readVarUhInt()
      if(self.firstCharacterMaxWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.firstCharacterMaxWeight) + ") on element of ExchangeStartedWithPodsMessage.firstCharacterMaxWeight.")
   
   def _secondCharacterIdFunc(self,input) :
      self.secondCharacterId = input.readDouble()
      if(self.secondCharacterId < -9007199254740992 or self.secondCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.secondCharacterId) + ") on element of ExchangeStartedWithPodsMessage.secondCharacterId.")
   
   def _secondCharacterCurrentWeightFunc(self,input) :
      self.secondCharacterCurrentWeight = input.readVarUhInt()
      if(self.secondCharacterCurrentWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.secondCharacterCurrentWeight) + ") on element of ExchangeStartedWithPodsMessage.secondCharacterCurrentWeight.")
   
   def _secondCharacterMaxWeightFunc(self,input) :
      self.secondCharacterMaxWeight = input.readVarUhInt()
      if(self.secondCharacterMaxWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.secondCharacterMaxWeight) + ") on element of ExchangeStartedWithPodsMessage.secondCharacterMaxWeight.")

   def resume(self):
      super().resume()
      print("firstCharacterId :",self.firstCharacterId)
      print("firstCharacterCurrentWeight :",self.firstCharacterCurrentWeight)
      print("firstCharacterMaxWeight :",self.firstCharacterMaxWeight)
      print("secondCharacterId :",self.secondCharacterId)
      print("secondCharacterCurrentWeight :",self.secondCharacterCurrentWeight)
      print("secondCharacterMaxWeight :",self.secondCharacterMaxWeight)
