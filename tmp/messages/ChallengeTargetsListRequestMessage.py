class ChallengeTargetsListRequestMessage:
   def __init__(self,input):
      self._challengeIdFunc(input)
   
   def _challengeIdFunc(self,input) :
      self.challengeId = input.readVarUhShort()
      if(self.challengeId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.challengeId) + ") on element of ChallengeTargetsListRequestMessage.challengeId.")

   def resume(self):
      print("challengeId :",self.challengeId)
