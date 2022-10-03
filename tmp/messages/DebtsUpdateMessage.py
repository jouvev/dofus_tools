import tmp.TypesFactory as pf
class DebtsUpdateMessage:
   def __init__(self,input):
      self.debts = []
      _id2 = 0
      _item2 = None
      self._actionFunc(input)
      _debtsLen = input.readUnsignedShort()
      for _i2 in range(0,_debtsLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.debts.append(_item2)
   
   def _actionFunc(self,input) :
      self.action = input.readByte()
      if(self.action < 0) :
         raise RuntimeError("Forbidden value (" + self.action + ") on element of DebtsUpdateMessage.action.")