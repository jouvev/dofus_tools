from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations

class BreachInvitationOfferMessage:
   def __init__(self,input):
      self.host = CharacterMinimalInformations(input)
      self._timeLeftBeforeCancelFunc(input)
   
   def _timeLeftBeforeCancelFunc(self,input) :
      self.timeLeftBeforeCancel = input.readVarUhInt()
      if(self.timeLeftBeforeCancel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.timeLeftBeforeCancel) + ") on element of BreachInvitationOfferMessage.timeLeftBeforeCancel.")

   def resume(self):
      print("timeLeftBeforeCancel :",self.timeLeftBeforeCancel)
      self.host.resum()
