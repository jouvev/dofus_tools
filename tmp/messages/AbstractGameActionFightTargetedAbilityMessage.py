from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._targetIdFunc(input)
      self._destinationCellIdFunc(input)
      self._criticalFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.silentCast = bool(bin(_box0)[2:].zfill(8)[0])
      self.verboseCast = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of AbstractGameActionFightTargetedAbilityMessage.targetId.")
   
   def _destinationCellIdFunc(self,input) :
      self.destinationCellId = input.readShort()
      if(self.destinationCellId < -1 or self.destinationCellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.destinationCellId) + ") on element of AbstractGameActionFightTargetedAbilityMessage.destinationCellId.")
   
   def _criticalFunc(self,input) :
      self.critical = input.readByte()
      if(self.critical < 0) :
         raise RuntimeError("Forbidden value (" + str(self.critical) + ") on element of AbstractGameActionFightTargetedAbilityMessage.critical.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("destinationCellId :",self.destinationCellId)
      print("critical :",self.critical)
