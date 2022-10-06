class ChallengeResultMessage:
   def __init__(self,input):
      self._challengeIdFunc(input)
      self._successFunc(input)
   
   def _challengeIdFunc(self,input) :
      self.challengeId = input.readVarUhShort()
      if(self.challengeId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.challengeId) + ") on element of ChallengeResultMessage.challengeId.")
   
   def _successFunc(self,input) :
      self.success = input.readBoolean()

   def resume(self):
      print("challengeId :",self.challengeId)
      print("success :",self.success)
