class ExchangeWaitingResultMessage:
   def __init__(self,input):
      self._bwaitFunc(input)
   
   def _bwaitFunc(self,input) :
      self.bwait = input.readBoolean()

   def resume(self):
      print("bwait :",self.bwait)
