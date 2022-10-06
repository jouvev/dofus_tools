class GameActionFightCastOnTargetRequestMessage:
   def __init__(self,input):
      self._spellIdFunc(input)
      self._targetIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of GameActionFightCastOnTargetRequestMessage.spellId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightCastOnTargetRequestMessage.targetId.")

   def resume(self):
      print("spellId :",self.spellId)
      print("targetId :",self.targetId)
