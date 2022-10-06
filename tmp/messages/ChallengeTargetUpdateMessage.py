class ChallengeTargetUpdateMessage:
   def __init__(self,input):
      self._challengeIdFunc(input)
      self._targetIdFunc(input)
   
   def _challengeIdFunc(self,input) :
      self.challengeId = input.readVarUhShort()
      if(self.challengeId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.challengeId) + ") on element of ChallengeTargetUpdateMessage.challengeId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of ChallengeTargetUpdateMessage.targetId.")

   def resume(self):
      print("challengeId :",self.challengeId)
      print("targetId :",self.targetId)
