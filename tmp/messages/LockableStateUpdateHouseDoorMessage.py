from tmp.messages.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage

class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
   def __init__(self,input):
      super().__init__(input)
      self._houseIdFunc(input)
      self._instanceIdFunc(input)
      self._secondHandFunc(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element of LockableStateUpdateHouseDoorMessage.houseId.")
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of LockableStateUpdateHouseDoorMessage.instanceId.")
   
   def _secondHandFunc(self,input) :
      self.secondHand = input.readBoolean()

   def resume(self):
      super().resume()
      print("houseId :",self.houseId)
      print("instanceId :",self.instanceId)
      print("secondHand :",self.secondHand)
