class ChallengeInfoMessage:
   def __init__(self,input):
      self._challengeIdFunc(input)
      self._targetIdFunc(input)
      self._xpBonusFunc(input)
      self._dropBonusFunc(input)
   
   def _challengeIdFunc(self,input) :
      self.challengeId = input.readVarUhShort()
      if(self.challengeId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.challengeId) + ") on element of ChallengeInfoMessage.challengeId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of ChallengeInfoMessage.targetId.")
   
   def _xpBonusFunc(self,input) :
      self.xpBonus = input.readVarUhInt()
      if(self.xpBonus < 0) :
         raise RuntimeError("Forbidden value (" + str(self.xpBonus) + ") on element of ChallengeInfoMessage.xpBonus.")
   
   def _dropBonusFunc(self,input) :
      self.dropBonus = input.readVarUhInt()
      if(self.dropBonus < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dropBonus) + ") on element of ChallengeInfoMessage.dropBonus.")

   def resume(self):
      print("challengeId :",self.challengeId)
      print("targetId :",self.targetId)
      print("xpBonus :",self.xpBonus)
      print("dropBonus :",self.dropBonus)
