class AbstractFightDispellableEffect:
   def __init__(self,input):
      self._uidFunc(input)
      self._targetIdFunc(input)
      self._turnDurationFunc(input)
      self._dispelableFunc(input)
      self._spellIdFunc(input)
      self._effectIdFunc(input)
      self._parentBoostUidFunc(input)
   
   def _uidFunc(self,input) :
      self.uid = input.readVarUhInt()
      if(self.uid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of AbstractFightDispellableEffect.uid.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of AbstractFightDispellableEffect.targetId.")
   
   def _turnDurationFunc(self,input) :
      self.turnDuration = input.readShort()
   
   def _dispelableFunc(self,input) :
      self.dispelable = input.readByte()
      if(self.dispelable < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dispelable) + ") on element of AbstractFightDispellableEffect.dispelable.")
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of AbstractFightDispellableEffect.spellId.")
   
   def _effectIdFunc(self,input) :
      self.effectId = input.readVarUhInt()
      if(self.effectId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.effectId) + ") on element of AbstractFightDispellableEffect.effectId.")
   
   def _parentBoostUidFunc(self,input) :
      self.parentBoostUid = input.readVarUhInt()
      if(self.parentBoostUid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.parentBoostUid) + ") on element of AbstractFightDispellableEffect.parentBoostUid.")

   def resume(self):
      print("uid :",self.uid)
      print("targetId :",self.targetId)
      print("turnDuration :",self.turnDuration)
      print("dispelable :",self.dispelable)
      print("spellId :",self.spellId)
      print("effectId :",self.effectId)
      print("parentBoostUid :",self.parentBoostUid)
