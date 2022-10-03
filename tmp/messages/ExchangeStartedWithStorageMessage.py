from tmp.messages.ExchangeStartedMessage import ExchangeStartedMessage
class ExchangeStartedWithStorageMessage(ExchangeStartedMessage):
   def __init__(self,input):
      super().__init__(input)
      self._storageMaxSlotFunc(input)
   
   def _storageMaxSlotFunc(self,input) :
      self.storageMaxSlot = input.readVarUhInt()
      if(self.storageMaxSlot < 0) :
         raise RuntimeError("Forbidden value (" + self.storageMaxSlot + ") on element of ExchangeStartedWithStorageMessage.storageMaxSlot.")