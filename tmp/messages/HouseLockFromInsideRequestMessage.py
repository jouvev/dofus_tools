from tmp.messages.LockableChangeCodeMessage import LockableChangeCodeMessage

class HouseLockFromInsideRequestMessage(LockableChangeCodeMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
