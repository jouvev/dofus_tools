from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations
class BreachInvitationResponseMessage:
   def __init__(self,input):
      self.guest = CharacterMinimalInformations(input)
      self._acceptFunc(input)
   
   def _acceptFunc(self,input) :
      self.accept = input.readBoolean()