class DebtsDeleteMessage:
   def __init__(self,input):
      self.debts = []
      _val2 = None
      self._reasonFunc(input)
      _debtsLen = input.readUnsignedShort()
      for _i2 in range(0,_debtsLen):
         _val2 = input.readDouble()
         if(_val2 < 0 or _val2 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of debts.")
         self.debts.append(_val2)
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()
      if(self.reason < 0) :
         raise RuntimeError("Forbidden value (" + str(self.reason) + ") on element of DebtsDeleteMessage.reason.")

   def resume(self):
      print("reason :",self.reason)
      print("debts :",self.debts)
