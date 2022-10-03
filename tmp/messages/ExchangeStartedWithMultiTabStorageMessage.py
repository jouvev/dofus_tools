from tmp.messages.ExchangeStartedMessage import ExchangeStartedMessage
class ExchangeStartedWithMultiTabStorageMessage(ExchangeStartedMessage):
   def __init__(self,input):
      super().__init__(input)
      self._storageMaxSlotFunc(input)
      self._tabNumberFunc(input)
   
   def _storageMaxSlotFunc(self,input) :
      self.storageMaxSlot = input.readVarUhInt()
      if(self.storageMaxSlot < 0) :
         raise RuntimeError("Forbidden value (" + self.storageMaxSlot + ") on element of ExchangeStartedWithMultiTabStorageMessage.storageMaxSlot.")
   
   def _tabNumberFunc(self,input) :
      self.tabNumber = input.readVarUhInt()
      if(self.tabNumber < 0) :
         raise RuntimeError("Forbidden value (" + self.tabNumber + ") on element of ExchangeStartedWithMultiTabStorageMessage.tabNumber.")