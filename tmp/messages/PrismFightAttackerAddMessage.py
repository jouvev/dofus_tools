import tmp.TypesFactory as pf

class PrismFightAttackerAddMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._fightIdFunc(input)
      _id3 = input.readUnsignedShort()
      self.attacker = pf.TypesFactory.get_instance_id(_id3,input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismFightAttackerAddMessage.subAreaId.")
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of PrismFightAttackerAddMessage.fightId.")

   def resume(self):
      print("subAreaId :",self.subAreaId)
      print("fightId :",self.fightId)
