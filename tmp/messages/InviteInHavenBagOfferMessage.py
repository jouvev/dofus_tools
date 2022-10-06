from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations

class InviteInHavenBagOfferMessage:
   def __init__(self,input):
      self.hostInformations = CharacterMinimalInformations(input)
      self._timeLeftBeforeCancelFunc(input)
   
   def _timeLeftBeforeCancelFunc(self,input) :
      self.timeLeftBeforeCancel = input.readVarInt()

   def resume(self):
      print("timeLeftBeforeCancel :",self.timeLeftBeforeCancel)
      self.hostInformations.resum()
