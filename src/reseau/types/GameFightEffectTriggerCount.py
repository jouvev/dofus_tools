class GameFightEffectTriggerCount:
   def __init__(self,input):
      self._effectIdFunc(input)
      self._targetIdFunc(input)
      self._countFunc(input)
   
   def _effectIdFunc(self,input) :
      self.effectId = input.readVarUhInt()
      if(self.effectId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.effectId) + ") on element of GameFightEffectTriggerCount.effectId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameFightEffectTriggerCount.targetId.")
   
   def _countFunc(self,input) :
      self.count = input.readByte()
      if(self.count < 0) :
         raise RuntimeError("Forbidden value (" + str(self.count) + ") on element of GameFightEffectTriggerCount.count.")

   def resume(self):
      print("effectId :",self.effectId)
      print("targetId :",self.targetId)
      print("count :",self.count)
