class ChallengeTargetsListRequestMessage:
   def __init__(self,input):
      self._challengeIdFunc(input)
   
   def _challengeIdFunc(self,input) :
      self.challengeId = input.readVarUhShort()
      if(self.challengeId < 0) :
         raise RuntimeError("Forbidden value (" + self.challengeId + ") on element of ChallengeTargetsListRequestMessage.challengeId.")